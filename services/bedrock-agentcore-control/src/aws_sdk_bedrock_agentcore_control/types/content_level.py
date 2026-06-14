"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ContentLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ContentLevel: TypeAlias = Literal[
    "METADATA_ONLY",
    "FULL_CONTENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "METADATA_ONLY",
        "FULL_CONTENT",
    )
)


def serialize_json(value: ContentLevel) -> str:
    return value


def deserialize_json(data: str) -> ContentLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentLevel value: {data!r}")
    return cast(ContentLevel, data)
