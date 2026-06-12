"""Generated from Smithy shape ``com.amazonaws.opensearch#Issues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.issue

Issues: TypeAlias = list["aws_sdk_opensearch.types.issue.Issue"]


# --- restJson1 ser/de ---
def serialize_json(value: Issues) -> list:
    return list(value)


def deserialize_json(data: list) -> Issues:
    return list(data)
