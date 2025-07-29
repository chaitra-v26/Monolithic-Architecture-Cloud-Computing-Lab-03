# Monolithic Architecture - Cloud Computing Lab 03

## 📋 Project Overview

This project demonstrates a **Monolithic Application** using the analogy of "The Great Indian Paratha" - a comprehensive Flask-based e-commerce application that showcases the characteristics, advantages, and disadvantages of monolithic architecture.

### 🥙 The Paratha Analogy

Imagine walking into a dhaba, and the cook serves you a massive paratha stuffed with aloo, paneer, gobhi, and even some leftover dal from last night. That's your monolithic application—one big, all-inclusive piece of software. It has everything: the dough (UI), the stuffing (business logic), and the ghee on top (data layer).

At first glance, it looks great - one wholesome package, easy to eat, and no extra plates. But when it's time to break it apart or make changes (like adding some green chilies), you realize things aren't as simple as they seemed.

## 🎯 Learning Objectives

- Understand monolithic application architecture
- Experience the advantages and challenges of monolithic systems
- Learn performance optimization techniques
- Implement load testing using Locust
- Practice debugging and fixing issues in tightly coupled systems

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend Framework** | Flask (Python) |
| **Frontend** | HTML, CSS, JavaScript |
| **Database** | SQLite3 |
| **Load Testing** | Locust |
| **Environment** | Python Virtual Environment |
| **Version Control** | Git & GitHub |


## ✨ Features

### Core Functionality
- **User Registration & Authentication**
- **Product Browsing** with detailed product views
- **Shopping Cart Management**
- **Checkout Process**
- **Database Integration** with SQLite

### Performance Features
- **Load Testing** with Locust integration
- **Code Optimization** for cart, checkout, and browse routes
- **Performance Monitoring** and metrics

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Linux environment (Ubuntu/WSL recommended)
- Git installed

> ⚠️ **Important**: If you're using Windows, please use WSL (Windows Subsystem for Linux) or a Linux Virtual Machine. Native Windows may lead to compatibility issues.

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/chaitra-v26/Monolithic-Architecture-Cloud-Computing-Lab-03.git
   cd Monolithic-Architecture-Cloud-Computing-Lab-03
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows WSL: source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Application**
   - Open `main.py`
   - Update the SRN on line 15 with your Student Registration Number

5. **Initialize Database**
   ```bash
   python3 insert_product.py
   ```

6. **Start the Application**
   ```bash
   python3 main.py
   ```

The application will be available at `http://localhost:5000`

## 🌐 Application Routes

| Route | Description | Method |
|-------|-------------|--------|
| `/register` | User registration | GET, POST |
| `/login` | User authentication | GET, POST |
| `/browse` | Browse products | GET |
| `/product/<id>` | Product details | GET |
| `/cart` | View shopping cart | GET |
| `/checkout` | Checkout process | GET, POST |

## 🧪 Load Testing with Locust

### Setup Load Testing

1. **Ensure main application is running**
   ```bash
   python3 main.py
   ```

2. **Run Locust (in a new terminal with venv activated)**
   ```bash
   # For checkout route testing
   locust -f locust/checkout-locustfile.py
   
   # For cart route testing
   locust -f locust/get-cart-locustfile.py
   
   # For browse route testing
   locust -f locust/browse-locustfile.py
   ```

3. **Access Locust Web Interface**
   - Open `http://localhost:8089`
   - Configure users, ramp-up rate, and test duration
   - Monitor performance metrics in real-time

### Performance Optimization Results

| Route | Before Optimization | After Optimization | Improvement |
|-------|-------------------|-------------------|-------------|
| `/checkout` | 176 requests | ~352 requests | ~100% increase |
| `/cart` | 1824 requests | ~3648 requests | ~100% increase |
| `/browse` | 2311 requests | ~4622 requests | ~100% increase |

## 🔧 Code Optimizations Implemented

### 1. Checkout Route Optimization
**Before:**
```python
for item in cart:
    while(item.cost > 0):
        total += 1
        item.cost -= 1
```

**After:**
```python
for item in cart:
    total += item.cost
```

### 2. Cart Route Optimization
- Replaced `eval()` with `json.loads()` for security
- Implemented product caching with dictionary lookup
- Combined nested loops into list comprehension
- Added type hints and documentation

### 3. Browse Route Optimization
- Used `@staticmethod` decorator for utility methods
- Implemented list comprehension for better performance
- Added comprehensive docstrings
- Removed unused imports

## 🏗️ Monolithic Architecture: Advantages & Disadvantages

### ✅ Advantages

1. **Simple and Straightforward**
   - Single codebase, easy to develop and deploy
   - Great for beginners and small teams

2. **Efficient Communication**
   - All components tightly integrated
   - No API overhead between modules

3. **Easier Debugging**
   - All code in one place
   - Simplified troubleshooting process

4. **Perfect for Small Teams**
   - Single developer can handle entire application
   - Quick delivery for limited resources

### ❌ Disadvantages

1. **Scaling Struggles**
   - Difficult to scale individual components
   - Changes affect entire application

2. **Deployment Drama**
   - Must redeploy entire application for small changes
   - Longer deployment times

3. **Not Flexible with Custom Requirements**
   - Cannot separate or modularize components easily
   - All-or-nothing approach

4. **Maintenance Challenges**
   - Large codebase becomes difficult to manage
   - Team coordination issues

5. **Single Point of Failure**
   - One component failure can bring down entire system
   - High risk of system-wide outages

## 🐛 Common Issues & Solutions

### Issue 1: Server Crash on Checkout
**Problem**: Intentional bug in checkout route causing server crash
**Solution**: Comment out line 16 in `checkout/__init__.py`

### Issue 2: Port Already in Use
**Problem**: Flask app cannot start on port 5000
**Solution**: 
```bash
# Kill process using port 5000
sudo lsof -t -i tcp:5000 | xargs kill -9
```

### Issue 3: Virtual Environment Issues
**Problem**: Module not found errors
**Solution**: Ensure virtual environment is activated
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## 📊 Performance Metrics

The application includes comprehensive performance monitoring through Locust, measuring:
- **Requests per second (RPS)**
- **Average response time**
- **95th percentile response time**
- **Error rates**
- **Concurrent user handling**

## 🚀 Future Enhancements

- Migration to microservices architecture (Thali approach)
- Implementation of Docker containerization
- Addition of Redis caching layer
- Enhanced error handling and logging
- API documentation with Swagger
- Unit and integration testing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 Lab Report Summary

This project successfully demonstrates:
- ✅ Understanding of monolithic architecture principles
- ✅ Hands-on experience with Flask application development
- ✅ Performance optimization techniques implementation
- ✅ Load testing with Locust framework
- ✅ Debugging and problem-solving in monolithic systems

---

> **The Verdict**: Monolithic applications are like a hearty paratha-simple, satisfying, and perfect for small setups. But as your needs grow, and your customers (users) demand variety, you may want to switch to a thali (microservices)—where each dish (service) is prepared and served separately. 🥘
