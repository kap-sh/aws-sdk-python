"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AttributeType``."""

from typing import Literal, TypeAlias, cast

AttributeType: TypeAlias = Literal[
    "STRING",
    "NUMBER",
    "BOOLEAN",
    "STRING_LIST",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeType) -> str:
    return value


def deserialize_json(data: str) -> AttributeType:
    return cast(AttributeType, data)
