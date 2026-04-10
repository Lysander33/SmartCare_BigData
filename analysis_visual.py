import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

def generate_insights(csv_path):
    # 读取分析后的结果数据
    df = pd.read_csv(csv_path)

    # 创建 2x2 的画布
    fig, axes = plt.subplots(1, 1, figsize=(10, 6))

    # 示例：各服务类型热度分析 (对应报告图11)
    sns.barplot(x='service_type', y='service_count', data=df, palette='viridis')
    plt.title('智慧医养服务类型热度分布')
    plt.xlabel('服务类型')
    plt.ylabel('频次')

    plt.tight_layout()
    plt.savefig('service_analysis.png')
    plt.show()

# 注意：运行前需要从 Hive 导出部分汇总数据为 CSV
# generate_insights('summary_data.csv')
