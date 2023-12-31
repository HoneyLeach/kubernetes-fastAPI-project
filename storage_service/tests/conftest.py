import asyncio

import pytest
from fastapi.testclient import TestClient

from storage_service.main import app
from storage_service.settings.core import cache, cache_meta


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def cleanup_cache():
    """Clear the cache after each test"""

    yield
    asyncio.run(cache.clear())
    cache_meta.clear()
