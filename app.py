
from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
def read_health():
    return {'status': 'healthy'}

# Additional endpoints can be added here as needed
