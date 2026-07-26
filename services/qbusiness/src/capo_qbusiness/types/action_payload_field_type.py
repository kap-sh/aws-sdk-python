"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionPayloadFieldType``."""

from typing import Literal, TypeAlias, cast

ActionPayloadFieldType: TypeAlias = Literal[
    "STRING",
    "NUMBER",
    "ARRAY",
    "BOOLEAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionPayloadFieldType) -> str:
    return value


def deserialize_json(data: str) -> ActionPayloadFieldType:
    return cast(ActionPayloadFieldType, data)
