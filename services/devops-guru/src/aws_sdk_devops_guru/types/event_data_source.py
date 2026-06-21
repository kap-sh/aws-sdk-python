"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventDataSource``."""

from typing import Literal, TypeAlias, cast

EventDataSource: TypeAlias = Literal[
    "AWS_CLOUD_TRAIL",
    "AWS_CODE_DEPLOY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventDataSource) -> str:
    return value


def deserialize_json(data: str) -> EventDataSource:
    return cast(EventDataSource, data)
