import pandas as pd

# Đọc file CSV
df = pd.read_csv("F:/athletics_analysis/analysis/merge_spr.csv")

# Chuẩn hóa kiểu dữ liệu
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["results_score"] = pd.to_numeric(df["results_score"], errors="coerce")

# Lọc sprints
df_spr = df[df["event_type"] == "sprints"].copy()

# Tạo cột year
df_spr["year"] = df_spr["date"].dt.year

# Loại dòng thiếu dữ liệu quan trọng
df_spr = df_spr.dropna(subset=["year", "results_score"])

# Đổi year về integer
df_spr["year"] = df_spr["year"].astype(int)

# Với mỗi năm, lấy dòng có results_score cao nhất
idx = df_spr.groupby("year")["results_score"].idxmax()

spr_top_row_by_year = (
    df_spr
    .loc[idx, [
        "year",
        "results_score",
        "event",
        "event_name",
        "competitor",
        "nat",
        "mark",
        "date",
        "venue",
        "gender",
        "environment",
        "age",
        "age_category"
    ]]
    .rename(columns={"results_score": "max_results_score"})
    .sort_values("year")
)

# Xuất file CSV
spr_top_row_by_year.to_csv(
    "spr_top_row_by_year.csv",
    index=False,
    encoding="utf-8-sig"
)

print(spr_top_row_by_year.head())
print(spr_top_row_by_year.tail())