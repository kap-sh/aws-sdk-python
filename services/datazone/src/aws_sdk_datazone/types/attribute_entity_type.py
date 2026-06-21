"""Generated from Smithy shape ``com.amazonaws.datazone#AttributeEntityType``."""

from typing import Literal, TypeAlias, cast

AttributeEntityType: TypeAlias = Literal[
    "ASSET",
    "LISTING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeEntityType) -> str:
    return value


def deserialize_json(data: str) -> AttributeEntityType:
    return cast(AttributeEntityType, data)
