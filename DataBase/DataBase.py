import psycopg2
from psycopg2.extras import DictCursor

class RegisterDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost", 
            database="investimentos",
            user="postgres",
            password="1234"
        )

    def query(self, query):
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query)
            
            if query.strip().lower().startswith("select"):
                return cur.fetchall()
            
            self.conn.commit()
            return "Query executada com sucesso!"
    
    def close(self):
        if self.conn:
            self.conn.close()


