# Flask Shop

A Flask-based e-commerce website with product management, shopping cart, and order processing.

## 中文说明

### 项目简介
Flask Shop是一个基于Flask框架开发的电子商务网站，具有产品管理、购物车和订单处理功能。

### 技术架构

#### 后端技术栈
- Python 3.x
- Flask 1.1.1
- Flask-SQLAlchemy
- Flask-Security (用户认证和授权)
- Flask-Mail (邮件功能)
- Flask-Babel (国际化)
- Flask-Uploads (文件上传)
- PostgreSQL (数据库)

#### 前端技术栈
- HTML5
- CSS3
- Jinja2模板引擎

### 功能模块

1. **用户管理**
   - 用户注册和登录
   - 角色管理（买家和卖家）
   - 个人信息管理
   - 地址管理

2. **产品管理**
   - 卖家上传和管理产品
   - 产品图片上传
   - 产品搜索和浏览

3. **订单管理**
   - 添加产品到购物车
   - 订单创建和管理
   - 订单状态跟踪
   - 支付流程

4. **系统管理**
   - 数据库初始化
   - 国际化支持
   - 文件上传管理

### 数据库设计

主要表结构：
- `user` - 用户信息
- `role` - 角色信息
- `role_user` - 用户角色关联
- `address` - 地址信息
- `product` - 产品信息
- `order` - 订单信息
- `bought_product` - 订单产品关联

### 快速开始

#### 环境要求
- Python 3.x
- PostgreSQL数据库

#### 安装步骤

1. 克隆仓库
```bash
git clone https://github.com/sangjiexun/Flask-Shop.git
cd Flask-Shop
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置数据库
修改 `flask_shop.py` 中的数据库连接信息：
```python
SQLALCHEMY_DATABASE_URI='postgresql://shop_writer:your_password@localhost:5432/shop'
```

4. 初始化数据库
```bash
flask initdb
```

5. 启动应用
```bash
python flask_shop.py
```

#### 测试账户
默认测试卖家账户：
- 邮箱：fake@example.com
- 密码：CHANGE_ME Password789

### 项目结构

```
Flask-Shop/
├── flask_shop/
│   ├── static/          # 静态文件
│   ├── templates/       # 模板文件
│   │   ├── security/    # 安全相关模板
│   │   ├── buy.html     # 购买页面
│   │   ├── layout.html  # 布局模板
│   │   ├── order.html   # 订单详情页面
│   │   ├── orders.html  # 订单列表页面
│   │   ├── pay.html     # 支付页面
│   │   ├── product.html # 产品详情页面
│   │   ├── search.html  # 搜索结果页面
│   │   └── sell.html    # 卖家产品上传页面
│   ├── __init__.py
│   ├── flask_shop.py    # 主应用文件
│   └── requirements.txt # 依赖文件
├── tests/               # 测试文件
├── LICENSE
├── README.md
└── setup.py
```

### 主要API

- `GET /` - 首页，显示产品列表
- `GET /product/sell` - 卖家上传产品页面
- `POST /product/sell` - 上传产品
- `POST /product/buy` - 添加产品到购物车
- `GET /product/<id>` - 产品详情页面
- `GET /order/<id>` - 订单详情页面
- `GET /orders_buyer` - 买家订单列表
- `GET /orders_seller` - 卖家订单列表
- `GET /order/pay` - 支付页面
- `POST /order/pay` - 提交支付

## English Documentation

### Project Introduction
Flask Shop is a Flask-based e-commerce website with product management, shopping cart, and order processing functionality.

### Technical Architecture

#### Backend Technology Stack
- Python 3.x
- Flask 1.1.1
- Flask-SQLAlchemy
- Flask-Security (user authentication and authorization)
- Flask-Mail (email functionality)
- Flask-Babel (internationalization)
- Flask-Uploads (file uploads)
- PostgreSQL (database)

#### Frontend Technology Stack
- HTML5
- CSS3
- Jinja2 template engine

### Feature Modules

1. **User Management**
   - User registration and login
   - Role management (buyer and seller)
   - Personal information management
   - Address management

2. **Product Management**
   - Sellers upload and manage products
   - Product image uploads
   - Product search and browsing

3. **Order Management**
   - Add products to cart
   - Order creation and management
   - Order status tracking
   - Payment process

4. **System Management**
   - Database initialization
   - Internationalization support
   - File upload management

### Database Design

Main tables:
- `user` - User information
- `role` - Role information
- `role_user` - User-role association
- `address` - Address information
- `product` - Product information
- `order` - Order information
- `bought_product` - Order-product association

### Quick Start

#### Requirements
- Python 3.x
- PostgreSQL database

#### Installation Steps

1. Clone the repository
```bash
git clone https://github.com/sangjiexun/Flask-Shop.git
cd Flask-Shop
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure database
Modify database connection in `flask_shop.py`:
```python
SQLALCHEMY_DATABASE_URI='postgresql://shop_writer:your_password@localhost:5432/shop'
```

4. Initialize database
```bash
flask initdb
```

5. Start the application
```bash
python flask_shop.py
```

#### Test Account
Default test seller account:
- Email: fake@example.com
- Password: CHANGE_ME Password789

### Project Structure

```
Flask-Shop/
├── flask_shop/
│   ├── static/          # Static files
│   ├── templates/       # Template files
│   │   ├── security/    # Security-related templates
│   │   ├── buy.html     # Buy page
│   │   ├── layout.html  # Layout template
│   │   ├── order.html   # Order detail page
│   │   ├── orders.html  # Order list page
│   │   ├── pay.html     # Payment page
│   │   ├── product.html # Product detail page
│   │   ├── search.html  # Search result page
│   │   └── sell.html    # Seller product upload page
│   ├── __init__.py
│   ├── flask_shop.py    # Main application file
│   └── requirements.txt # Dependency file
├── tests/               # Test files
├── LICENSE
├── README.md
└── setup.py
```

### Main APIs

- `GET /` - Home page, display product list
- `GET /product/sell` - Seller product upload page
- `POST /product/sell` - Upload product
- `POST /product/buy` - Add product to cart
- `GET /product/<id>` - Product detail page
- `GET /order/<id>` - Order detail page
- `GET /orders_buyer` - Buyer order list
- `GET /orders_seller` - Seller order list
- `GET /order/pay` - Payment page
- `POST /order/pay` - Submit payment

## License

This project is licensed under the MIT License - see the LICENSE file for details.