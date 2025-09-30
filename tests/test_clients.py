import pytest
from app import clients
from app.clients import fetch_topics, fetch_skills, fetch_resources
from app.clients import TOPICS_API_BASE_URL, RESOURCES_API_BASE_URL


class _Capture:
    def __init__(self):
        self.calls = []


def test_fetch_topics_calls_expected_url(monkeypatch):
    cap = _Capture()

    def mock_get_json(url):
        cap.calls.append(url)
        return [{"id": "t1", "name": "Topic 1"}]
    
    monkeypatch.setattr(clients, "get_json", mock_get_json)

    result = fetch_topics()
    expected_url = f"{TOPICS_API_BASE_URL}/topics"

    assert cap.calls == [expected_url]
    assert result == [{"id": "t1", "name": "Topic 1"}]


def test_fetch_skills_calls_expected_url(monkeypatch):
    cap = _Capture()

    def mock_get_json(url):
        cap.calls.append(url)
        return [{"id": "s1", "name": "Skill 1"}]
    
    monkeypatch.setattr(clients, "get_json", mock_get_json)

    result = fetch_skills()
    expected_url = f"{TOPICS_API_BASE_URL}/skills"

    assert cap.calls == [expected_url]
    assert result == [{"id": "s1", "name": "Skill 1"}]


def test_fetch_resources_calls_expected_url(monkeypatch):
    cap = _Capture()

    def mock_get_json(url):
        cap.calls.append(url)
        return [{"id": "r1", "title": "Resource 1"}]
    
    monkeypatch.setattr(clients, "get_json", mock_get_json)

    result = fetch_resources()
    expected_url = f"{RESOURCES_API_BASE_URL}/resources"

    assert cap.calls == [expected_url]
    assert result == [{"id": "r1", "title": "Resource 1"}]
