# Introduction to Pandas
# 10-13

test=food_info.columns.tolist()
gram_columns =[]
for i in test:
    if i.endswith("(g)"):
        gram_columns.append(i)
gram_df = food_info[gram_columns]


