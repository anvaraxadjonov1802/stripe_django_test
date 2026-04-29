# Django Stripe Checkout — Full Documentation

This is a simple Django application integrated with Stripe Checkout.

The project was built as a Python Developer test task.

Users can open an item page, click the **Buy** button, and complete payment using **Stripe Checkout**.

---

## Features

- Django project structure
- `Item` model
- Django Admin panel
- Stripe Checkout Session creation
- Product detail page
- JavaScript redirect to Stripe Checkout
- Success page
- Cancel page
- Environment variables support
- Basic Stripe error handling
- Currency field for items
- Docker support
- SQLite database for local development

---

## Demo Admin Access

```txt
Admin URL: /admin/
Login: user
Password: user
```

For local development:

```txt
http://127.0.0.1:8000/admin/
```

---

## Technologies

- Python
- Django
- Stripe API
- SQLite
- HTML
- CSS
- JavaScript
- Docker
- python-dotenv

---

## Project Structure

```txt
stripe_django_test/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── shop/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── shop/
│           ├── item_detail.html
│           ├── success.html
│           └── cancel.html
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
├── README.md
└── README_FULL.md
```

---

## Main Endpoints

### Item Detail Page

```txt
GET /item/{id}
```

Example:

```txt
http://127.0.0.1:8000/item/1
```

This page displays item information and a **Buy** button.

---

### Buy Endpoint

```txt
GET /buy/{id}
```

This endpoint creates a Stripe Checkout Session and returns the session ID.

Example response:

```json
{
  "id": "cs_test_..."
}
```

The frontend uses this session ID to redirect the user to Stripe Checkout.

---

### Success Page

```txt
/success/
```

User is redirected here after successful payment.

---

### Cancel Page

```txt
/cancel/
```

User is redirected here if payment is cancelled.

---

## Payment Flow

1. User opens `/item/{id}`.
2. User clicks the **Buy** button.
3. Frontend sends request to `/buy/{id}`.
4. Django creates Stripe Checkout Session.
5. Backend returns Stripe Session ID.
6. JavaScript redirects user to Stripe Checkout.
7. After payment:
   - success → `/success/`
   - cancel → `/cancel/`

---

## Requirements

Make sure you have installed:

- Python 3.10+
- pip
- virtualenv
- Stripe account

---

## Installation

### 1. Clone repository

```bash
git clone your_repository_url
cd stripe_django_test
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

---

### 3. Activate virtual environment

Linux / macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env` file:

```bash
cp .env.example .env
```

Example `.env`:

```env
DJANGO_SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

STRIPE_SECRET_KEY=sk_test_your_secret_key
STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key

DOMAIN=http://127.0.0.1:8000
```

Stripe keys can be found in Stripe Dashboard:

```txt
Developers → API keys
```

Use only test keys for local development:

```txt
sk_test_...
pk_test_...
```

Do not commit `.env` to GitHub.

---

## Database Setup

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

---

## Create Demo Admin User

Use this command to create admin user:

```bash
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u, _ = User.objects.get_or_create(username='user'); u.is_staff = True; u.is_superuser = True; u.set_password('user'); u.save(); print('Demo admin user is ready')"
```

Credentials:

```txt
Login: user
Password: user
```

---

## Run Project

```bash
python manage.py runserver
```

Open:

```txt
http://127.0.0.1:8000/admin/
```

If port `8000` is busy:

```bash
python manage.py runserver 8001
```

Then update `.env`:

```env
DOMAIN=http://127.0.0.1:8001
```

---

## Add Test Item

Open admin panel:

```txt
http://127.0.0.1:8000/admin/
```

Create a new item:

```txt
Name: Test Product
Description: This is a test product
Price: 10.00
Currency: USD
```

Then open:

```txt
http://127.0.0.1:8000/item/1
```

---

## Stripe Test Payment

Use this test card:

```txt
4242 4242 4242 4242
```

Other values:

```txt
Expiry date: Any future date
CVC: Any 3 digits
ZIP / Postal code: Any value
```

Example:

```txt
Card number: 4242 4242 4242 4242
Expiry: 12/34
CVC: 123
ZIP: 10000
```

No real money will be charged in test mode.

---

## Docker Setup

Build and run project:

```bash
docker compose up --build
```

Run migrations inside Docker:

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

Create demo admin user inside Docker:

```bash
docker compose exec web python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u, _ = User.objects.get_or_create(username='user'); u.is_staff = True; u.is_superuser = True; u.set_password('user'); u.save(); print('Demo admin user is ready')"
```

Open:

```txt
http://127.0.0.1:8000/admin/
```

Stop containers:

```bash
docker compose down
```

---

## Common Errors

### Port already in use

```txt
Error: That port is already in use.
```

Fix:

```bash
python manage.py runserver 8001
```

Update `.env`:

```env
DOMAIN=http://127.0.0.1:8001
```

---

### Invalid Stripe API Key

Fix:

- Check `.env`
- Make sure `STRIPE_SECRET_KEY` starts with `sk_test_`
- Restart server

```bash
CTRL + C
python manage.py runserver
```

---

### Checkout does not redirect

Make sure `DOMAIN` matches your running server.

Example:

```env
DOMAIN=http://127.0.0.1:8000
```

---

## Git Ignore

`.gitignore` should include:

```gitignore
venv/
.env
db.sqlite3
__pycache__/
*.pyc
.idea/
.vscode/
```

---

## Completed Requirements

- Django backend
- Stripe API integration
- `Item` model
- `GET /item/{id}`
- `GET /buy/{id}`
- Stripe Checkout Session creation
- HTML page with Buy button
- Stripe redirect
- Django Admin panel
- Admin credentials for testing
- Environment variables
- Docker support

---

## Author

Created by Anvar Axadjonov as a Python Developer test task.