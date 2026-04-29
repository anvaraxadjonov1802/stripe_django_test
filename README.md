# Django Stripe Checkout

A simple Django application integrated with Stripe Checkout.

Users can open an item page, click the **Buy** button, and pay through **Stripe Checkout**.

---

## Features

- Django backend
- Stripe Checkout integration
- `Item` model
- Django Admin panel
- Product detail page
- Buy button with Stripe redirect
- Success and cancel pages
- Environment variables support
- Docker support

---

## Demo Admin Access

```txt
Admin URL: /admin/
Login: user
Password: user
```

---

## Main URLs

```txt
/item/{id}     - item detail page
/buy/{id}      - creates Stripe Checkout Session
/success/      - successful payment page
/cancel/       - cancelled payment page
/admin/        - Django Admin panel
```

Example:

```txt
http://127.0.0.1:8000/item/1
```

---

## Quick Start

Clone project:

```bash
git clone your_repository_url
cd stripe_django_test
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```bash
cp .env.example .env
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create demo admin user:

```bash
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u, _ = User.objects.get_or_create(username='user'); u.is_staff = True; u.is_superuser = True; u.set_password('user'); u.save(); print('Demo admin user is ready')"
```

Run server:

```bash
python manage.py runserver
```

Open:

```txt
http://127.0.0.1:8000/admin/
```

---

## Stripe Test Card

```txt
Card number: 4242 4242 4242 4242
Expiry: Any future date
CVC: Any 3 digits
ZIP: Any value
```

---

## Environment Variables

Example `.env`:

```env
DJANGO_SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

STRIPE_SECRET_KEY=sk_test_your_secret_key
STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key

DOMAIN=http://127.0.0.1:8000
```

---

## Docker

Run with Docker:

```bash
docker compose up --build
```

Run migrations:

```bash
docker compose exec web python manage.py migrate
```

Create demo admin user:

```bash
docker compose exec web python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u, _ = User.objects.get_or_create(username='user'); u.is_staff = True; u.is_superuser = True; u.set_password('user'); u.save(); print('Demo admin user is ready')"
```

---

## Detailed Documentation

Detailed setup instructions are available in:

```txt
README_FULL.md
```