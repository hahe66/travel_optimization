# plot_budget.py
import matplotlib.pyplot as plt
from data import CITIES
from solver import evaluate_city
import matplotlib.ticker as ticker

# 1. 设置全局字体和高级样式
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():
    budgets = list(range(1500, 2101, 10)) 
    
    xiamen, changsha, guilin = [], [], []

    for budget in budgets:
        for city_name, city_data in CITIES.items():
            best, _ = evaluate_city(city_name, city_data, budget=budget)
            interest = best["interest"] if best else 0
            if city_name == "厦门": xiamen.append(interest)
            elif city_name == "长沙": changsha.append(interest)
            elif city_name == "桂林": guilin.append(interest)

    # 2. 创建画布并设置高级灰白背景
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#F8F9FA')
    ax.set_facecolor('#FFFFFF') # 绘图区纯白

    # 3. 绘制直角阶梯线 (step-post 表示预算达标后立刻跃升)
    # 颜色换成更有质感的：厦门(天蓝), 长沙(琥珀), 桂林(珊瑚红)
    ax.step(budgets, xiamen, label="厦门", color="#4A90E2", linewidth=3, where='post', alpha=0.9)
    ax.step(budgets, changsha, label="长沙", color="#F5A623", linewidth=3, where='post', alpha=0.9)
    ax.step(budgets, guilin, label="桂林", color="#D0021B", linewidth=3, where='post', alpha=0.9)

    # 4. 添加精美的标注框（去掉丑陋的箭头，改用带圆角的文字框）
    bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="#D0021B", lw=1.5, alpha=0.9)
    ax.annotate('预算 1610 元\n桂林反超', xy=(1610, 36), xytext=(1620, 31),
                arrowprops=dict(arrowstyle="->", color="#D0021B", lw=1.5),
                fontsize=11, fontweight='bold', color="#D0021B", bbox=bbox_props)

    bbox_props2 = dict(boxstyle="round,pad=0.5", fc="white", ec="#F5A623", lw=1.5, alpha=0.9)
    ax.annotate('预算 1784 元\n长沙反超', xy=(1784, 37), xytext=(1820, 32),
                arrowprops=dict(arrowstyle="->", color="#F5A623", lw=1.5),
                fontsize=11, fontweight='bold', color="#F5A623", bbox=bbox_props2)

    # 5. 图表装饰
    ax.set_title("不同预算下各城市总兴趣对比", fontsize=16, fontweight='bold', pad=20, color='#333333')
    ax.set_xlabel("总预算 (元)", fontsize=13, color='#555555')
    ax.set_ylabel("总兴趣值 (分)", fontsize=13, color='#555555')

    # 去掉顶部和右侧的边框线（极简风）
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#DDDDDD')
    ax.spines['bottom'].set_color('#DDDDDD')

    # 6. 网格线：只保留水平网格，虚线，极淡
    ax.yaxis.grid(True, linestyle='--', alpha=0.5, color='#DDDDDD')
    ax.xaxis.grid(False)

    # 7. 坐标轴刻度
    ax.set_xlim(1500, 2100)
    ax.set_ylim(20, 40)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(2))

    # 8. 图例：去掉边框，移到右下角
    ax.legend(fontsize=12, loc='lower right', frameon=False)

    plt.tight_layout()
    plt.savefig("fig1_budget_sensitivity.png", dpi=300, bbox_inches='tight', facecolor='#F8F9FA')
    print("✅ 高级美化版图表已生成并保存！请打开文件夹查看图片。")
    plt.show()

if __name__ == "__main__":
    main()