"""Generated from Smithy shape ``com.amazonaws.qbusiness#ResponseScope``."""

from typing import Literal, TypeAlias, cast

ResponseScope: TypeAlias = Literal[
    "ENTERPRISE_CONTENT_ONLY",
    "EXTENDED_KNOWLEDGE_ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseScope) -> str:
    return value


def deserialize_json(data: str) -> ResponseScope:
    return cast(ResponseScope, data)
