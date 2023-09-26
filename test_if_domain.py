#! /usr/bin/env python3
# -*- coding:utf-8 -*-


def is_invalid_domain(string) -> set:
    e = set(c for c in string if not (c.isalnum() or c in ["-", "."]))
    print(e)
    return e


def is_valid_domain(string) -> bool:
    for c in string:
        if not (c.isalnum() or c in ["-", "."]):
            return False
    return True


def main():
    domains = set(
        ["aaa.bb.cc", "aa_.test.com", "*.*.domain.com", "%20%20fesses.sexy.cul"]
    )
    valid_domains = set()
    invalid_domains = set()

    for domain in domains:
        if is_invalid_domain(domain):
            invalid_domains.add(domain)
        elif is_invalid_domain():
            valid_domains.add(domain)

    print("valid domains :")
    print(valid_domains)
    print("invalid domains :")
    print(invalid_domains)


if __name__ == "__main__":
    main()
