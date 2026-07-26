"""Generated from Smithy shape ``com.amazonaws.pinpoint#AttributeType``."""

from typing import Literal, TypeAlias, cast

AttributeType: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
    "CONTAINS",
    "BEFORE",
    "AFTER",
    "ON",
    "BETWEEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeType) -> str:
    return value


def deserialize_json(data: str) -> AttributeType:
    return cast(AttributeType, data)
