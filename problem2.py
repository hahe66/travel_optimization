# problem2.py
# 问题二：预算敏感性分析
from data import CITIES
from solver import evaluate_city

def main():
    print("开始进行预算敏感性扫描 (1500元 - 2100元)...")
    print("-" * 50)
    
    # 记录上一个预算的最佳方案，用于找出“关键预算值”
    last_best_city = None
    last_best_interest = None
    
    # 预算从 1500 到 2100，步长为 1（精细扫描找临界点）
    # 如果想跑快一点，可以把步长改为 10
    for budget in range(1500, 2101, 1):
        city_results = []
        
        # 遍历三个城市，获取当前预算下的最优解
        for city_name, city_data in CITIES.items():
            best, _ = evaluate_city(city_name, city_data, budget=budget)
            if best is not None:
                city_results.append(best)
                
        # 如果三个城市当前预算下都去不了（无可行方案）
        if not city_results:
            continue
            
        # 找出现在所有可行城市中，全局最优的那个
        global_best = min(
            city_results,
            key=lambda x: (-x["interest"], x["cost"], x["time"])
        )
        
        # 如果发现最佳目的地变了，或者最佳兴趣值变了，说明遇到了关键转折点
        if (global_best["city"] != last_best_city) or (global_best["interest"] != last_best_interest):
            print(f"【关键节点】预算达到 {budget} 元时：")
            print(f"  最佳目的地：{global_best['city']}")
            print(f"  最优组合：{'、'.join(global_best['selected'])}")
            print(f"  总费用：{global_best['cost']} 元")
            print(f"  总时间：{global_best['time']:.2f} 小时")
            print(f"  总兴趣值：{global_best['interest']} 分\n")
            
            # 更新状态
            last_best_city = global_best["city"]
            last_best_interest = global_best["interest"]

if __name__ == "__main__":
    main()