
[app]

# 应用名称
title = YourAppName

# 包名，通常采用反向域名风格命名
package.name = com.yourcompany.yourapp

# 应用版本号
package.version = 0.1

# 应用图标（可选，如果不需要可以注释掉）
#icon.filename = %(source.dir)s/data/icon.png

[buildozer]

# 指定构建目标为安卓
target = android

# 选择要使用的 Python 版本
android.p4a.python_version = 3.9

# 设置最低安卓版本要求（可选，根据需求调整）
android.minapi = 21

# 设置目标安卓版本（可选，根据需求调整）
android.sdk = 33
android.ndk = 21.4.7075529
android.ant = /usr/bin/ant

# 设置日志级别（可选）
log_level = 2

source.dir =.


