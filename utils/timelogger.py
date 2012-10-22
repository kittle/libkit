import time


class timelogger():

    def __init__(self, log_pre, log, logstr):
        self.log_pre = log_pre
        self.log = log
        self.logstr = logstr

    def __enter__(self):
        if self.log_pre:
            self.log_pre("Start: " + self.logstr)
        self.s_time = time.time()
        return self

    def __exit__(self, _type, value, traceback):
        self.e_time = time.time()
        self.duration = self.e_time - self.s_time
        if not _type:
            if self.log:
                self.log("Finish: %s . Execution time: %.2f sec" % (
                                            self.logstr, self.duration))
