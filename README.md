# trails
A simple implementation of trailing-based state restoration

https://mail.python.org/pipermail/python-ideas/2015-December/037475.html

trails.py implements SAVEANT Pierre's API exactly (plus a "reset"
function to start over between tests).

scopedtrails.py implements simple "manual scoping".

Since the first API doesn't provide any way to mark a variable as
deleted or created, but the second one pretty much requires that, I
just did something hacky and used `None` to mean undefined. If you
actually want o store `None` values, that obviously doesn't work. It
would be easy to fix that; I was just trying to implement as much as I
could in 10 minutes. :)

I believe both will work back to 3.0 as-is, and back to 2.4 or so
(whenever `@property` was added) if you just add `(object)` to all
class definitions to force them to be new-style classes.
