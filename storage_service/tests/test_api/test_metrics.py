import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_metrics(client):
    """Checking GET /metrics request for Prometheus"""

    response = client.get('/metrics')

    assert response.status_code == status.HTTP_200_OK
    assert response.content is not None
