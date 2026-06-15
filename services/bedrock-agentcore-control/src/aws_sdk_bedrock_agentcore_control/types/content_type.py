"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ContentType: TypeAlias = Literal["MEMORY_RECORDS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MEMORY_RECORDS",))


def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentType value: {data!r}")
    return cast(ContentType, data)
