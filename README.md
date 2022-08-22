# URLbuilder
Script to generate a URL list to scan / fuzz from a network address. It works with a single IP or domain but the purpose is over a network address

This is the first version of this single script. I created because I wanted to have some cool time programming, there could be way more better approaches than this simple script.

```
usage: URLbuilder.py [-h] [--output OUTPUT] [--noslash] [--noredirect] input
```
# Pending Updates

I am aware of some improvements that I am planning on doing to this script, I detail them below:

- I plan to add a validation regarding the protocol. It starts with HTTP, and redirects to HTTPS if the server does that. There are cases when there is no redirect but the host has HTTPS, I will be thinking for a way to solve this.

- Duplicate URLs may appear, there is no a work around so far for this

- I am planning to introduce a parameter for the request timeout 

- I might be adding some headers if needed or test with different HTTP versions
