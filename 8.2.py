import pyodbc

class ReusablePool:
    """
    Manage Reusable objects for use by Client objects.
    """
 
    def __init__(self, size):
        reusables = Reusable(size)
        self._reusables = reusables.return_row()
 
    def acquire(self):
        return self._reusables.pop()
 
    def release(self, reusable):
        self._reusables.append(reusable)
        
    
 
class Reusable:
    def __init__(self, size)
        driver = 'DRIVER={SQL Server}'
        server = 'SERVER=localhost'
        port = 'PORT=1433'
        db = 'DATABASE=testdb'
        user = 'UID=me'
        pw = 'PWD=pass'
        conn_str = ';'.join([driver, server, port, db, user, pw])
         
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
         
        cursor.execute('select * from table_name')
        row = cursor.fetchmany(size)
        
    def return_row ()
        return row
 

 
def main():
    reusable_pool = ReusablePool(10)
    reusable = reusable_pool.acquire()
    reusable_pool.release(reusable)
 
 
if __name__ == "__main__":
    main()