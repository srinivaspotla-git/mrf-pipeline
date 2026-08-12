import duckdb

con = duckdb.connect()

READ_OPTS = """
    read_csv('data/raw/seton_hays.csv',
        skip=2, header=true, all_varchar=true,
        sample_size=-1, ignore_errors=true, strict_mode=false)
"""

# row_count = con.sql(f"SELECT COUNT(*) FROM {READ_OPTS}").fetchone()[0]
# print(f"Rows parsed: {row_count:,}")

# print("\n--- Payers by row count ---")
# print(con.sql(f"""
#     SELECT payer_name, COUNT(*) AS n
#     FROM {READ_OPTS}
#     GROUP BY payer_name
#     ORDER BY n DESC
#     LIMIT 30
# """))

payer_count = con.sql(f"SELECT COUNT(distinct payer_name) FROM {READ_OPTS}").fetchone()[0]
print(f"Distinct Payers: {payer_count:,}")

