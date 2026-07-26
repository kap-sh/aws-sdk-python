"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttributeType``."""

from typing import Literal, TypeAlias, cast

AttributeType: TypeAlias = Literal[
    "STRING",
    "STRING_LIST",
    "NUMBER",
    "DATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeType) -> str:
    return value


def deserialize_json(data: str) -> AttributeType:
    return cast(AttributeType, data)
