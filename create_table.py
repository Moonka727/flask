from db import get_db_connection

def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS links (
            id SERIAL PRIMARY KEY,
            short_code VARCHAR(10) UNIQUE NOT NULL,
            original_url TEXT NOT NULL,
            used BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP NOT NULL,
            used_at TIMESTAMP NULL
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Таблица создана!")

if __name__ == '__main__':
    create_table()
