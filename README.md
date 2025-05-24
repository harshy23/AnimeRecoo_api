# AnimeReco API

A Django REST API for anime recommendations and management.

## 1. How to Set Up and Run the Project Locally

### Prerequisites
- Python 3.8+
- pip


### Steps
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd AnimeRecoo_api
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # or
   source venv/bin/activate   # On Mac/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Create a superuser (for admin access):**
   ```sh
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
7. **Access the API:**
   - API root: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 2. REST API Endpoints

| Method | Endpoint             | Description                        |
|--------|----------------------|------------------------------------|
| POST   | /login/              | Register a new user                |
| GET    | /search/?q=...       | Search for anime                   |
| POST   | /recommendations/    | Get anime recommendations          |
| POST   | /preferences/        | Set user genre preferences         |
| POST   | /token/              | Obtain JWT token                   |
| POST   | /token/refresh/      | Refresh JWT token                  |

---

## 3. Sample Requests and Responses

### Register a New User
**Request:**
```http
POST /login/
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}
```
**Response:**
```json
{
  "message": "User created successfully"
}
```

---

### Search for Anime
**Request:**
```http
GET /search/?q=naruto
Authorization: Bearer <access_token>
```
**Response:**
```json
[
  {
    "id": 1,
    "title": "Naruto",
    "genre": "Action",
    "episodes": 220
  }
]
```

---

### Get Recommendations
**Request:**
```http
POST /recommendations/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "user_id": 1
}
```
**Response:**
```json
[
  {
    "id": 2,
    "title": "Attack on Titan",
    "genre": "Action",
    "episodes": 75
  }
]
```

---

### Set User Preferences
**Request:**
```http
POST /preferences/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "genres": ["Action", "Adventure"]
}
```
**Response:**
```json
{
  "message": "Preferences updated"
}
```

---

### Obtain JWT Token
**Request:**
```http
POST /token/
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}
```
**Response:**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

---

For more details, visit your deployed API at:  
https://animerecoo-api.onrender.com

## Admin Panel
- Visit `/admin/` to manage data via Django admin (login required).

## Static Files
- Static files are served via WhiteNoise in production. Run `python manage.py collectstatic` before deploying.

---

**Contact:** For questions, open an issue or contact the maintainer.
