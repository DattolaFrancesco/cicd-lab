from starlette.testclient import TestClient
from app.main import app

client = TestClient(app=app)
def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

