"""Generated from Smithy shape ``com.amazonaws.iot#DynamoKeyType``."""

from typing import Literal, TypeAlias, cast

DynamoKeyType: TypeAlias = Literal[
    "STRING",
    "NUMBER",
]


# --- restJson1 ser/de ---
def serialize_json(value: DynamoKeyType) -> str:
    return value


def deserialize_json(data: str) -> DynamoKeyType:
    return cast(DynamoKeyType, data)
