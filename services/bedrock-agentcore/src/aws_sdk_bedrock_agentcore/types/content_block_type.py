"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ContentBlockType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

ContentBlockType: TypeAlias = Literal[
    "text",
    "image",
    "resource",
    "resource_link",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "text",
        "image",
        "resource",
        "resource_link",
    )
)


def serialize_json(value: ContentBlockType) -> str:
    return value


def deserialize_json(data: str) -> ContentBlockType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentBlockType value: {data!r}")
    return cast(ContentBlockType, data)
