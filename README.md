Test | Expected | wget | curl | py_requests | ruby | go | nim
--- | --- | --- | --- | --- | --- | --- | ---
[expired](https://expired.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[wrong.host](https://wrong.host.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | 🔴
[self-signed](https://self-signed.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[untrusted-root](https://untrusted-root.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[revoked](https://revoked.badssl.com/) | bad | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[pinning-test](https://pinning-test.badssl.com/) | bad | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[no-common-name](https://no-common-name.badssl.com/) | dubious | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[no-subject](https://no-subject.badssl.com/) | dubious | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[incomplete-chain](https://incomplete-chain.badssl.com/) | dubious | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[sha1-intermediate](https://sha1-intermediate.badssl.com/) | bad | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[sha256](https://sha256.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[sha384](https://sha384.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[sha512](https://sha512.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[1000-sans](https://1000-sans.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[10000-sans](https://10000-sans.badssl.com/) | good | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[ecc256](https://ecc256.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[ecc384](https://ecc384.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[rsa2048](https://rsa2048.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[rsa8192](https://rsa8192.badssl.com/) | dubious | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[regular http](http://http.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[http on https URL](https://http.badssl.com/) | bad | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[cbc](https://cbc.badssl.com/) | dubious | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[rc4-md5](https://rc4-md5.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[rc4](https://rc4.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[3des](https://3des.badssl.com/) | bad | 🔴 | ✓ | ✓ | ✓ | 🔴 | ✓
[null](https://null.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | 🔴
[mozilla-old](https://mozilla-old.badssl.com/) | bad | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[mozilla-intermediate](https://mozilla-intermediate.badssl.com/) | dubious | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[mozilla-modern](https://mozilla-modern.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[dh480](https://dh480.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[dh512](https://dh512.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[dh1024](https://dh1024.badssl.com/) | dubious | 🔴 | 🔴 | 🔴 | 🔴 | ✓ | 🔴
[dh2048](https://dh2048.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | 🔴 | ✓
[dh-small-subgroup](https://dh-small-subgroup.badssl.com/) | bad | 🔴 | 🔴 | 🔴 | 🔴 | ✓ | 🔴
[dh-composite](https://dh-composite.badssl.com/) | bad | 🔴 | 🔴 | 🔴 | 🔴 | ✓ | 🔴
[static-rsa](https://static-rsa.badssl.com/) | dubious | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[tls-v1-0](https://tls-v1-0.badssl.com:1010/) | dubious | 🔴 | 🔴 | ✓ | 🔴 | 🔴 | 🔴
[tls-v1-1](https://tls-v1-1.badssl.com:1011/) | dubious | 🔴 | 🔴 | ✓ | 🔴 | 🔴 | 🔴
[invalid-expected-sct](https://invalid-expected-sct.badssl.com/) | bad | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴
[hsts](https://hsts.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[upgrade](https://upgrade.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[preloaded-hsts](https://preloaded-hsts.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[subdomain.preloaded-...](https://subdomain.preloaded-hsts.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[https-everywhere](https://https-everywhere.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[long-extended-subdom...](https://long-extended-subdomain-name-containing-many-letters-and-dashes.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[longextendedsubdomai...](https://longextendedsubdomainnamewithoutdashesinordertotestwordwrapping.badssl.com/) | good | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[(Lenovo) Superfish](https://superfish.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[(Dell) eDellRoot](https://edellroot.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[(Dell) DSD Test Prov...](https://dsdtestprovider.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[preact-cli](https://preact-cli.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[webpack-dev-server](https://webpack-dev-server.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[captive-portal](https://captive-portal.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | 🔴
[mitm-software](https://mitm-software.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[sha1-2016](https://sha1-2016.badssl.com/) | dubious | ✓ | ✓ | ✓ | ✓ | ✓ | ✓
[sha1-2017](https://sha1-2017.badssl.com/) | bad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓