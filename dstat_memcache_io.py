### Author: Dean Wilson <dean.wilson@gmail.com>

class dstat_plugin(dstat):
    """
    Memcache network io plugin.

    Displays the number of bytes read and written.
    """
    def __init__(self):
        self.name = 'memcache/io'
        self.nick = ('read', 'write')
        self.vars = ('bytes_read', 'bytes_written')
        self.type = 'd'
        self.width = 5
        self.scale = 1024

    def check(self):
        try:
            global memcache
            import memcache
            self.mc = memcache.Client(['127.0.0.1:11211'], debug=0)
        except:
            raise Exception, 'Plugin needs the memcache module'

    def extract(self):
        stats = self.mc.get_stats()
        for name in self.vars:
            self.set2[name] = long(stats[0][1][name])
            self.val[name] = (self.set2[name] - self.set1[name]) * 1.0 / elapsed
        if step == op.delay:
            self.set1.update(self.set2)
