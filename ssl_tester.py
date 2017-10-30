#!/usr/bin/env python3
# Compare SSL implementations against badssl.com

import subprocess
import requests

tests = [
  ("https://expired.badssl.com/", "bad", "expired"),
  ("https://wrong.host.badssl.com/", "bad", "wrong.host"),
  ("https://self-signed.badssl.com/", "bad", "self-signed"),
  ("https://untrusted-root.badssl.com/", "bad", "untrusted-root"),
  ("https://revoked.badssl.com/", "bad", "revoked"),
  ("https://pinning-test.badssl.com/", "bad", "pinning-test"),
  ("https://no-common-name.badssl.com/", "dubious", "no-common-name"),
  ("https://no-subject.badssl.com/", "dubious", "no-subject"),
  ("https://incomplete-chain.badssl.com/", "dubious", "incomplete-chain"),
  ("https://sha1-intermediate.badssl.com/", "bad", "sha1-intermediate"),
  ("https://sha256.badssl.com/", "good", "sha256"),
  ("https://sha384.badssl.com/", "good", "sha384"),
  ("https://sha512.badssl.com/", "good", "sha512"),
  ("https://1000-sans.badssl.com/", "good", "1000-sans"),
  ("https://10000-sans.badssl.com/", "good", "10000-sans"),
  ("https://ecc256.badssl.com/", "good", "ecc256"),
  ("https://ecc384.badssl.com/", "good", "ecc384"),
  ("https://rsa2048.badssl.com/", "good", "rsa2048"),
  ("https://rsa8192.badssl.com/", "dubious", "rsa8192"),
  ("http://http.badssl.com/", "good", "regular http"),
  ("https://http.badssl.com/", "bad", "http on https URL"),
  ("https://cbc.badssl.com/", "dubious", "cbc"),
  ("https://rc4-md5.badssl.com/", "bad", "rc4-md5"),
  ("https://rc4.badssl.com/", "bad", "rc4"),
  ("https://3des.badssl.com/", "bad", "3des"),
  ("https://null.badssl.com/", "bad", "null"),
  ("https://mozilla-old.badssl.com/", "bad", "mozilla-old"),
  ("https://mozilla-intermediate.badssl.com/", "dubious", "mozilla-intermediate"),
  ("https://mozilla-modern.badssl.com/", "good", "mozilla-modern"),
  ("https://dh480.badssl.com/", "bad", "dh480"),
  ("https://dh512.badssl.com/", "bad", "dh512"),
  ("https://dh1024.badssl.com/", "dubious", "dh1024"),
  ("https://dh2048.badssl.com/", "good", "dh2048"),
  ("https://dh-small-subgroup.badssl.com/", "bad", "dh-small-subgroup"),
  ("https://dh-composite.badssl.com/", "bad", "dh-composite"),
  ("https://static-rsa.badssl.com/", "dubious", "static-rsa"),
  ("https://tls-v1-0.badssl.com:1010/", "dubious", "tls-v1-0"),
  ("https://tls-v1-1.badssl.com:1011/", "dubious", "tls-v1-1"),
  ("https://invalid-expected-sct.badssl.com/", "bad", "invalid-expected-sct"),
  ("https://hsts.badssl.com/", "good", "hsts"),
  ("https://upgrade.badssl.com/", "good", "upgrade"),
  ("https://preloaded-hsts.badssl.com/", "good", "preloaded-hsts"),
  ("https://subdomain.preloaded-hsts.badssl.com/", "bad", "subdomain.preloaded-hsts"),
  ("https://https-everywhere.badssl.com/", "good", "https-everywhere"),
  ("https://long-extended-subdomain-name-containing-many-letters-and-dashes.badssl.com/", "good",
    "long-extended-subdomain-name-containing-many-letters-and-dashes"),
  ("https://longextendedsubdomainnamewithoutdashesinordertotestwordwrapping.badssl.com/", "good",
    "longextendedsubdomainnamewithoutdashesinordertotestwordwrapping"),
  ("https://superfish.badssl.com/", "bad", "(Lenovo) Superfish"),
  ("https://edellroot.badssl.com/", "bad", "(Dell) eDellRoot"),
  ("https://dsdtestprovider.badssl.com/", "bad", "(Dell) DSD Test Provider"),
  ("https://preact-cli.badssl.com/", "bad", "preact-cli"),
  ("https://webpack-dev-server.badssl.com/", "bad", "webpack-dev-server"),
  ("https://captive-portal.badssl.com/", "bad", "captive-portal"),
  ("https://mitm-software.badssl.com/", "bad", "mitm-software"),
  ("https://sha1-2016.badssl.com/", "dubious", "sha1-2016"),
  ("https://sha1-2017.badssl.com/", "bad", "sha1-2017"),
]


# test wrappers


def wget(url):
    cmd = "wget --quiet %s -O /dev/null" % url
    subprocess.check_output(cmd, shell=True)


def curl(url):
    cmd = "curl -s %s -o /dev/null" % url
    subprocess.check_output(cmd, shell=True)


def py_requests(url):
    requests.get(url, verify=True)


def ruby(url):
    cmd = "ruby testers/tester_ruby.rb %s" % url
    subprocess.check_output(cmd, shell=True)


def go(url):
    cmd = "./testers/tester_go %s" % url
    subprocess.check_output(cmd, shell=True)


def nim(url):
    cmd = "./testers/tester_nim %s" % url
    subprocess.check_output(cmd, shell=True)


testers = (wget, curl, py_requests, ruby, go, nim)
tests = tests


def run_test(tester, url, category):
    print(tester.__name__, url, category)
    try:
        tester(url)
        raised = False
    except Exception as e:
        raised = True

    print("raised:", raised)
    o = (category != "good") == raised
    print("outcome:", "ok" if o else "FAIL")
    print()
    return o


def run_tests():
    out = []
    for url, category, desc in tests:
        out.append([])
        for tester in testers:
            outcome = run_test(tester, url, category)
            out[-1].append(outcome)

    return out


def render(outcomes):
    s = []
    headers = ['Test', 'Expected'] + [t.__name__ for t in testers]
    s.append(" | ".join(headers))
    s.append(" | ".join(['---'] * len(headers)))

    for test, outcomes_row in zip(tests, outcomes):
        url, category, desc = test
        if len(desc) > 20:
            desc = desc[:20] + "..."
        row = ["[{}]({})".format(desc, url), category]
        row += ["✓" if o else "🔴" for o in outcomes_row]
        s.append(" | ".join(row))

    s = "\n".join(s)
    print(s)
    return s


def main():
    out = run_tests()
    print()
    s = render(out)
    with open('README.md', 'w') as f:
        f.write(s)


if __name__ == '__main__':
    main()
