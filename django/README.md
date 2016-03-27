Django is so much boilerplate, right?
=====================================

**No.** Unless you use the project and app generators, wich you should; the
`settings.py` in here is insanely insecure.


So how small can it get?
------------------------

Assuming we want the `./manage.py runserver` command and a WSGI hook:
```bash
$ du --human-readable --summarize --apparent-size django/
4.3K    django/
```

To be fair we still end up with several files, so in reality it'll be something like

```bash
$ du --human-readable --summarize django/
32K     django/
```
