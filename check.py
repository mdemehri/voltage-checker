import csv

LOW = 4.75
HIGH = 5.25


def check_reading(text, low=LOW, high=HIGH):
    text = (text or "").strip()
    if text == "":
        return "MISSING"
    try:
        voltage = float(text)
    except ValueError:
        return "INVALID"
    if low <= voltage <= high:
        return "PASS"
    return "FAIL"


def main():
    counts = {"PASS": 0, "FAIL": 0, "MISSING": 0, "INVALID": 0}
    with open("readings.csv", newline="") as f:
        for row in csv.DictReader(f):
            result = check_reading(row.get("voltage"))
            counts[result] += 1
            print(row["board"], row.get("voltage"), result)
    print("Passed:", counts["PASS"], "Failed:", counts["FAIL"],
          "Missing/invalid:", counts["MISSING"] + counts["INVALID"])


if __name__ == "__main__":
    main()