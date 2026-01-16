from fastapi import header , HTTPException
from app.core.config import settings
from app.core.security import verify_token

def get_api_key(api_key: str = header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403,detail='Invalid API KEY')
    

def get_current_user(token: str = header(...)):
    if not payload:
        raise HTTPException(status_code=401,detail="Invalid jwt token")
    return payload