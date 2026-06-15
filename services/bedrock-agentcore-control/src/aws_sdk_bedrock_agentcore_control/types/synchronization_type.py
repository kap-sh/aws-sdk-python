"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SynchronizationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

SynchronizationType: TypeAlias = Literal["URL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("URL",))


def serialize_json(value: SynchronizationType) -> str:
    return value


def deserialize_json(data: str) -> SynchronizationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SynchronizationType value: {data!r}")
    return cast(SynchronizationType, data)
