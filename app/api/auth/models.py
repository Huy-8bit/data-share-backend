from pydantic import BaseModel


class RegistrationRequest(BaseModel):
    email: str
    username: str


class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class User(BaseModel):
    email: str
    access_token: str


class EmailRequest(BaseModel):
    email: str


class PasswordResetRequest(BaseModel):
    email: str


class PasswordResetModel(BaseModel):
    email: str
    verification_code: str
    new_password: str
