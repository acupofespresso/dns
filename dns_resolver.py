import dns.resolver
import socket
import time

def get_all_a_records(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [answer.address for answer in answers]
    except dns.resolver.NXDOMAIN:
        return f"Error: The domain '{domain}' does not exist."
    except dns.resolver.NoAnswer:
        return f"Error: The domain '{domain}' has no A records."
    except dns.exception.Timeout:
        return f"Error: Timeout while resolving '{domain}'."
    except Exception as e:
        return f"Error: {e}"

def get_cname_records(domain):
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        return [answer.target.to_text() for answer in answers]
    except dns.resolver.NXDOMAIN:
        return f"Error: The domain '{domain}' does not exist."
    except dns.resolver.NoAnswer:
        return f"Error: The domain '{domain}' has no CNAME records."
    except dns.exception.Timeout:
        return f"Error: Timeout while resolving '{domain}'."
    except Exception as e:
        return f"Error: {e}"

def test_latency(ip):
    try:
        import ping3
        return ping3.ping(ip) * 1000
    except Exception as e:
        return float('inf')

if __name__ == '__main__':
    domain = input('Enter the domain: ')
    cname_records = get_cname_records(domain)
    if isinstance(cname_records, list):
        all_a_records = []
        for cname in cname_records:
            a_records = get_all_a_records(cname)
            if isinstance(a_records, list):
                all_a_records.extend(a_records)
        if all_a_records:
            latency_results = [(ip, test_latency(ip)) for ip in all_a_records]
            sorted_ips = sorted(latency_results, key=lambda x: x[1])
            print(f'A records for {domain} sorted by latency:')
            for ip, latency in sorted_ips:
                print(f'{ip}: {latency} ms')
        else:
            print(f"Error: No A records found for CNAME targets of '{domain}'.")
    else:
        a_records = get_all_a_records(domain)
        if isinstance(a_records, list):
            latency_results = [(ip, test_latency(ip)) for ip in a_records]
            sorted_ips = sorted(latency_results, key=lambda x: x[1])
            print(f'A records for {domain} sorted by latency:')
            for ip, latency in sorted_ips:
                print(f'{ip}: {latency} ms')
        else:
            print(a_records)
