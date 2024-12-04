from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def menu_admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def numbr_user(user_id: int) -> dict:
    return {"Вы вошли как пользователь № ": user_id}

@app.get("/user/")
async def info_user(user_name: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {user_name}, Возраст: {age} "}