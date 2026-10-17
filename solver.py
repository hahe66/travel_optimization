# solver.py
import itertools
from data import CITIES, BUDGET, ACCOMMODATION


def evaluate_city(city_name, city_data, budget=BUDGET, time_factor=1.0):
    items = city_data["items"]
    n = len(items)

    best_plan = None
    feasible_count = 0

    for mask in itertools.product([0, 1], repeat=n):
        cost = sum(mask[i] * items[i]["cost"] for i in range(n))
        cost += city_data["transport"] + ACCOMMODATION

        time = sum(mask[i] * items[i]["time"] for i in range(n))
        time *= time_factor

        interest = sum(mask[i] * items[i]["interest"] for i in range(n))

        if cost <= budget and time <= city_data["available_time"]:
            feasible_count += 1
            selected = [items[i]["name"] for i in range(n) if mask[i] == 1]
            plan = {
                "city": city_name,
                "selected": selected,
                "cost": cost,
                "time": time,
                "interest": interest,
                "mask": mask,
            }

            if best_plan is None:
                best_plan = plan
            else:
                current_key = (-plan["interest"], plan["cost"], plan["time"])
                best_key = (-best_plan["interest"], best_plan["cost"], best_plan["time"])
                if current_key < best_key:
                    best_plan = plan

    return best_plan, feasible_count


def main():
    all_best = []

    for city_name, city_data in CITIES.items():
        best, count = evaluate_city(city_name, city_data)

        print(f"\n城市：{city_name}")
        if best is None:
            print("  无可行方案。")
            continue

        print(f"  可行方案数：{count}")
        print(f"  最优组合：{'、'.join(best['selected'])}")
        print(f"  总费用：{best['cost']} 元")
        print(f"  总时间：{best['time']:.2f} 小时")
        print(f"  总兴趣值：{best['interest']} 分")
        all_best.append(best)

    if all_best:
        global_best = min(
            all_best,
            key=lambda x: (-x["interest"], x["cost"], x["time"])
        )
        print("\n===== 全局最优 =====")
        print(f"目的地：{global_best['city']}")
        print(f"项目：{'、'.join(global_best['selected'])}")
        print(f"总费用：{global_best['cost']} 元")
        print(f"总时间：{global_best['time']:.2f} 小时")
        print(f"总兴趣值：{global_best['interest']} 分")


if __name__ == "__main__":
    main()