# data.py
# C题：短期旅行决策模型数据

BUDGET = 1800
ACCOMMODATION = 700  # 住宿及基本餐饮费统一 700 元

CITIES = {
    "厦门": {
        "available_time": 18,
        "transport": 456,
        "items": [
            {"name": "鼓浪屿", "cost": 35, "time": 6.0, "interest": 9},
            {"name": "厦门园林植物园", "cost": 15, "time": 4.0, "interest": 7},
            {"name": "胡里山炮台", "cost": 12, "time": 2.5, "interest": 5},
            {"name": "环岛路", "cost": 0, "time": 3.0, "interest": 8},
            {"name": "中山路夜游", "cost": 0, "time": 2.5, "interest": 6},
        ],
    },
    "长沙": {
        "available_time": 18,
        "transport": 884,
        "items": [
            {"name": "湖南博物院", "cost": 0, "time": 4.0, "interest": 10},
            {"name": "岳麓书院", "cost": 20, "time": 3.5, "interest": 9},
            {"name": "橘子洲", "cost": 0, "time": 3.0, "interest": 7},
            {"name": "黄兴路步行街", "cost": 0, "time": 2.5, "interest": 8},
            {"name": "长沙世界之窗", "cost": 180, "time": 7.0, "interest": 10},
        ],
    },
    "桂林": {
        "available_time": 16,
        "transport": 597,
        "items": [
            {"name": "漓江精华游", "cost": 188, "time": 6.0, "interest": 10},
            {"name": "象鼻山", "cost": 0, "time": 2.0, "interest": 6},
            {"name": "日游四湖", "cost": 80, "time": 1.5, "interest": 6},
            {"name": "芦笛岩", "cost": 45, "time": 3.0, "interest": 8},
            {"name": "东西巷", "cost": 0, "time": 2.0, "interest": 6},
        ],
    },
}