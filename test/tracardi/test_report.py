from pydantic import ValidationError
from tracardi.domain.report import Report


def test_report_entities():
    for entity in ("profile", "session", "event", "entity", "improper-value-1", "improper-value-2"):
        try:
            Report(
                id="@test-report",
                name="test-report",
                description="Here's report description.",
                entity=entity,
                query={"query": {"term": {"type": "{{type}}"}}},
                tags=["tag1", "tag2"]
            )

        except ValidationError as e:
            assert entity in ("improper-value-1", "improper-value-2")
