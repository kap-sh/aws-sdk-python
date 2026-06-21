"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PropertyValueType``."""

from typing import Literal, TypeAlias, cast

PropertyValueType: TypeAlias = Literal[
    "PLAIN_TEXT",
    "STRINGIFIED_JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValueType) -> str:
    return value


def deserialize_json(data: str) -> PropertyValueType:
    return cast(PropertyValueType, data)
