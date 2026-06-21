"""Generated from Smithy shape ``com.amazonaws.iot#FieldType``."""

from typing import Literal, TypeAlias, cast

FieldType: TypeAlias = Literal[
    "Number",
    "String",
    "Boolean",
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldType) -> str:
    return value


def deserialize_json(data: str) -> FieldType:
    return cast(FieldType, data)
