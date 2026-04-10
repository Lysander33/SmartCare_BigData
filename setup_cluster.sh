#!/bin/bash
# 智慧医养大数据环境初始化参考脚本

# 1. 环境变量配置参考
echo "export HADOOP_HOME=/opt/bigdata/hadoop/hadoop-3.3.5" >> /etc/profile
echo "export SPARK_HOME=/opt/bigdata/spark" >> /etc/profile
source /etc/profile

# 2. 关键节点配置
# hadoop01 (Master), hadoop02 (Worker), hadoop03 (Worker)

# 3. Hive Metastore 启动命令
# nohup hive --service metastore &
