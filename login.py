# 登录模块（模拟代码）
def login(username, password):
    """
    模拟用户登录验证
    :param username: 用户名
    :param password: 密码
    :return: 登录结果（字符串）
    """
    # 模拟数据库中的用户信息（实际项目中会连接数据库）
    valid_users = {
        "admin": "admin123",
        "user01": "user01@123"
    }
    
    # 验证逻辑
    if username not in valid_users:
        return f"错误：用户名 '{username}' 不存在"
    elif valid_users[username] != password:
        return "错误：密码不正确"
    else:
        return f"成功：用户 '{username}' 登录成功"


# 测试代码（可直接运行查看效果）
if __name__ == "__main__":
    print(login("admin", "admin123"))   # 预期输出：成功登录
    print(login("admin", "wrongpwd"))  # 预期输出：密码错误
    print(login("guest", "123"))       # 预期输出：用户名不存在
    