import pandas as pd

schedule = pd.DataFrame(
    {
        "hour": [19, 20, 21, 22],
        "NRK1": ["Dagsrevyen", "Beat for beat", "Nytt på nytt", "Lindmo"],
        "TV2": ["Kjære landsmenn", "Forræder", "21-nyhetene", "Farfar"],
        "TVNorge": [
            "The Big Bang Theory",
            "Alltid beredt",
            "Kongen befaler",
            "Praktisk info",
        ],
    }
)
