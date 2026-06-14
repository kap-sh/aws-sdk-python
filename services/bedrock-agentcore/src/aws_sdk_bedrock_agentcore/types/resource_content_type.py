"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResourceContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

ResourceContentType: TypeAlias = Literal[
    "text",
    "blob",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "text",
        "blob",
    )
)


def serialize_json(value: ResourceContentType) -> str:
    return value


def deserialize_json(data: str) -> ResourceContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceContentType value: {data!r}")
    return cast(ResourceContentType, data)
