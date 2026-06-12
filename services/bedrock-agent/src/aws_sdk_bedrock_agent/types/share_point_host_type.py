"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SharePointHostType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

SharePointHostType: TypeAlias = Literal["ONLINE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ONLINE",))


def serialize_json(value: SharePointHostType) -> str:
    return value


def deserialize_json(data: str) -> SharePointHostType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SharePointHostType value: {data!r}")
    return cast(SharePointHostType, data)
