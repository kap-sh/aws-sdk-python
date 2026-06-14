"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExceptionLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ExceptionLevel: TypeAlias = Literal["DEBUG",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEBUG",))


def serialize_json(value: ExceptionLevel) -> str:
    return value


def deserialize_json(data: str) -> ExceptionLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExceptionLevel value: {data!r}")
    return cast(ExceptionLevel, data)
