import threading
import random
import time

RAND_CEIL = 50      #   randomization threshold
WAIT_USR = 3
WAIT_SRVR = 1


class USER:
    _mut = []

    def __init__(self, webServer):
        """
        Initialization method, saves the web server received as an input
        :param webServer: object with the method of 'get'
        :return: None
        """
        self.server = webServer

    def request_page(self):
        """
        Requests a page (in this case, a number) from the server
        :return: None
        """
        rand = random.randint(0, RAND_CEIL)
        self.server.get(rand, self._mut)
        return None

    def user_op(self):
        """
        This method represents the user operations (just line printing)
        I added some sleep between prints for the output readability
        :return: None
        """
        while True:
            print 'User make op id:{0}\n'.format(random.randint(0, 10))
            time.sleep(WAIT_SRVR)   # done in order to keep the output readable

    def main_call(self):
        """
        This main call represents the user side, the user operations are running as a separated thread constantly
        while the requests are being sent one after another
        :return: None
        """
        t_user = threading.Thread(target=self.user_op)
        t_user.start()
        while True:
            t_server = threading.Thread(target=self.request_page)
            t_server.start()
            while True:
                if self._mut != []:
                    print 'Server replied {0}\n'.format(self._mut[0])
                    self._mut =[]
                    break
                else:
                    #   Let user thread to work a little longer before checking on server again
                    t_user.join(WAIT_USR)


class SERVER:

    def __init__(self):
        """
        Initializes the server with some random number
        :return:
        """
        self._rand = random.randint(0, RAND_CEIL)

    def get(self, num, mut):
        """
        This represents the server, trying to calculate some complicated multiplication
        :param num: some int from 0 to RAND_CEIL
        :param mut: the mutable object of the calling user
        :return:
        """
        mult = self._rand * num
        sum = 1
        for i in range(1, mult+1):
            sum *= i
        mut.append(sum)
        return None

if __name__ == '__main__':

    server = SERVER()
    user = USER(server)
    user.main_call()
