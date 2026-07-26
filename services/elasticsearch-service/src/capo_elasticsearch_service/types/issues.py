"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#Issues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.issue

Issues: TypeAlias = list["capo_elasticsearch_service.types.issue.Issue"]


# --- restJson1 ser/de ---
def serialize_json(value: Issues) -> list:
    return list(value)


def deserialize_json(data: list) -> Issues:
    return list(data)
