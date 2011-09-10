"""
Before you run this:

  $ git submodule init build/requirements

After you run this:

  $ cd build/requirements; git add index.html; git push
  $ cd ..; git add build/requirements; git push

"""

import os
import time

def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size

def write_index(path):
    fp = open(os.path.join(path, "index.html"), 'w')

    print >> fp, "<html><body><h1>Index of dist.socialplanning.org/%s</h1><table><tr><th>Filename</th><th>Size</th><th>Last Modified</th></tr>" % path

    dirs = []
    for filename in sorted(os.listdir(path)):
        if filename.startswith("."):
            continue
        print >> fp, """<tr><td><a href="/%s">%s</a></td>""" % (
            os.path.join(path, filename), filename)
        stat = os.stat(os.path.join(path, filename))
        print >> fp, """<td>%s</td><td>%s</td></tr>""" % (
            convert_bytes(stat.st_size),
            time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(stat.st_mtime)),
            )
        if os.path.isdir(os.path.join(path, filename)):
            dirs.append(os.path.join(path, filename))

    print >> fp, "</table></body></html>"
    fp.close()

    for path in dirs:
        write_index(path)

write_index("build/requirements")
