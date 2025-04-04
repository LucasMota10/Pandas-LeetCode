# **Pandas Functions**

## **Create df:** 

```
pd.DataFrame(Content,columns=["column1","column2"])
```

## **Number of Rows:**

```
df.shape[0]
```

## **Number of Columns:**

```
df.shape[1]
```

## **Print the first x rows:**

```
df.head(x)
```
## **Print the last x rows:**

```
df.tail(x)
```

## **Select a row by a Value:**

```
df.loc[df["Column Name"] == x]
df.loc[df["Column Name"] != x]
df.loc[df["Column Name"] > x]
df.loc[df["Column Name"] < x]
df.loc[df["Column Name"] >= x]
df.loc[df["Column Name"] <= x]
```

## **Create a New Column:**

```
df["New Column"] = Value
```

## **Drop Duplicate Rows:**

```
df.drop_duplicates("Column Name", keep="first/last/false")
```
