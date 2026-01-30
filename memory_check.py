import psutil
import sys

def check_memory(threshold_mb=4000):
    processes = []
    limit_exceeded = False

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            pinfo = proc.info
            mem_mb = pinfo['memory_info'].rss / (1024 * 1024)
            processes.append({'pid': pinfo['pid'], 'name': pinfo['name'], 'mem': mem_mb})
            if mem_mb > threshold_mb:
                limit_exceeded = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort and print
    sorted_proc = sorted(processes, key=lambda x: x['mem'], reverse=True)[:5]
    print(f"{'PID':<10} {'Name':<25} {'Memory':<10}")
    for p in sorted_proc:
        print(f"{p['pid']:<10} {p['name']:<25} {p['mem']:>8.2f} MB")

    if limit_exceeded:
        print("\n[ERROR] A process exceeded the memory threshold!")
        sys.exit(1) # This fails the Jenkins job

if __name__ == "__main__":
    check_memory()