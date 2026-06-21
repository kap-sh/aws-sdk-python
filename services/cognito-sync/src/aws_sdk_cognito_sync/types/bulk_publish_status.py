"""Generated from Smithy shape ``com.amazonaws.cognitosync#BulkPublishStatus``."""

from typing import Literal, TypeAlias, cast

BulkPublishStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BulkPublishStatus) -> str:
    return value


def deserialize_json(data: str) -> BulkPublishStatus:
    return cast(BulkPublishStatus, data)
