# 🗃️ Django Inventory API

A simple Django REST Framework-based Inventory API with JWT Authentication.

---

## 🚀 Features

- 🔐 **JWT Authentication** (Login & Token Refresh)
- 📦 **Inventory CRUD** using ViewSets and Routers
- 🔎 **Category-Based Filtering**
- 💰 **Price-Based Sorting**
- 🧾 **User Registration Endpoint**

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)

---

## 📂 API Endpoints

| Method | Endpoint                                 | Description                    |
|--------|------------------------------------------|--------------------------------|
| GET    | `/inventory/`                            | List all inventory items       |
| POST   | `/inventory/`                            | Create new inventory item      |
| GET    | `/inventory/{id}/`                       | Retrieve item by ID            |
| PUT    | `/inventory/{id}/`                       | Update item by ID              |
| DELETE | `/inventory/{id}/`                       | Delete item by ID              |
| GET    | `/inventory/category/<cg>/`              | Filter items by category       |
| GET    | `/inventory/price/sort/`                 | Sort items by price (low-high) |
| POST   | `/inventory/api/register`                | User registration              |
| POST   | `/inventory/api/token`                   | Obtain JWT access & refresh    |
| POST   | `/inventory/api/refresh`                 | Refresh JWT token              |

---

## 🧑‍💻 Installation

```bash
git clone https://github.com/MrDCooL/inventory-api.git
cd inventory-api
python -m venv venv
source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
