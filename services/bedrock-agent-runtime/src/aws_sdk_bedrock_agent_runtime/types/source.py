"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Source``."""

from typing import Literal, TypeAlias, cast

Source: TypeAlias = Literal[
    "ACTION_GROUP",
    "KNOWLEDGE_BASE",
    "PARSER",
]


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> str:
    return value


def deserialize_json(data: str) -> Source:
    return cast(Source, data)
