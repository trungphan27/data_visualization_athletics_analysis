from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
JUMP_DIR = BASE_DIR / "jump"

INPUT_FILES = [
    JUMP_DIR / "men_jump.csv",
    JUMP_DIR / "women_jump.csv",
]

OUTPUT_FILE = JUMP_DIR / "jump_top_score_by_year_gender.csv"


def load_jump_gender_files(input_files):
    frames = []

    for input_file in input_files:
        df = pd.read_csv(input_file)
        frames.append(df)

    return pd.concat(frames, ignore_index=True)


def build_top_score_by_year_gender(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["results_score"] = pd.to_numeric(df["results_score"], errors="coerce")
    df["year"] = df["date"].dt.year

    df = df.dropna(subset=["year", "gender", "results_score"])
    df["year"] = df["year"].astype(int)

    max_score = (
        df.groupby(["year", "gender"], as_index=False)["results_score"]
        .max()
        .rename(columns={"results_score": "max_results_score"})
    )

    result = df.merge(max_score, on=["year", "gender"], how="inner")
    result = result[result["results_score"] == result["max_results_score"]].copy()

    leading_cols = ["year", "gender", "max_results_score"]
    replaced_cols = ["results_score"]
    remaining_cols = [col for col in result.columns if col not in leading_cols]
    remaining_cols = [col for col in remaining_cols if col not in replaced_cols]

    return result[leading_cols + remaining_cols].sort_values(
        ["year", "gender", "event", "competitor", "date"],
        ascending=[True, True, True, True, True],
    )


def main():
    df = load_jump_gender_files(INPUT_FILES)
    top_score_by_year_gender = build_top_score_by_year_gender(df)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    top_score_by_year_gender.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

    print(f"Saved: {OUTPUT_FILE}")
    print(f"Rows: {len(top_score_by_year_gender)}")
    print(top_score_by_year_gender[["year", "gender", "max_results_score", "event", "mark", "competitor", "nat"]].head())
    print(top_score_by_year_gender[["year", "gender", "max_results_score", "event", "mark", "competitor", "nat"]].tail())


if __name__ == "__main__":
    main()
