from datetime import date, timedelta

_today = date.today()

def _days_ago(days: int) -> str:
    return (_today - timedelta(days=days)).isoformat()

users_data = {
    "user123": {
        "book": {
            "price": 23,
            "date": _days_ago(5),
        },
        "pen": {
            "price": 7,
            "date": _days_ago(7),
        },
    },
    "user124": {
        "notebook": {
            "price": 12,
            "date": _days_ago(10),
        },
    },
    "user125": {
        "pencil": {
            "price": 3,
            "date": _days_ago(5),
        },
        "ruler": {
            "price": 5,
            "date": _days_ago(40),
        },
    },
    "user126": {
        "backpack": {
            "price": 45,
            "date": _days_ago(10),
        },
        "water_bottle": {
            "price": 18,
            "date": _days_ago(90),
        },
        "lunch_box": {
            "price": 14,
            "date": _days_ago(12),
        },
    },
    "user127": {
        "eraser": {
            "price": 2,
            "date": _days_ago(15),
        },
    },
    "user128": {
        "stapler": {
            "price": 11,
            "date": _days_ago(12),
        },
        "highlighter": {
            "price": 4,
            "date": _days_ago(12),
        },
    },
    "user129": {
        "calculator": {
            "price": 29,
            "date": _days_ago(45),
        },
        "folder": {
            "price": 6,
            "date": _days_ago(10),
        },
        "usb_drive": {
            "price": 16,
            "date": _days_ago(65),
        },
    },
    "user130": {
        "headphones": {
            "price": 35,
            "date": _days_ago(15),
        },
    },
    "user131": {
        "desk_lamp": {
            "price": 28,
            "date": _days_ago(10),
        },
        "mouse": {
            "price": 20,
            "date": _days_ago(10),
        },
    },
    "user132": {
        "sketchbook": {
            "price": 17,
            "date": _days_ago(10),
        },
        "paintbrush": {
            "price": 9,
            "date": _days_ago(8),
        },
        "canvas": {
            "price": 25,
            "date": _days_ago(60),
        },
    },
}
