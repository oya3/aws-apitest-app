class DBInfo():
    def __init__(self):
        super().__init__()
        self.connections = {}
        self.connections['host'] = 'locahost'
        self.connections['port'] = 8081
        self.connections['dbname'] = 'dbname'
        self.connections['user'] = 'user'
        self.connections['password'] = 'password'
