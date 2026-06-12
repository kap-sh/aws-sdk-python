"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

StepType: TypeAlias = Literal["POST_CHUNKING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("POST_CHUNKING",))


def serialize_json(value: StepType) -> str:
    return value


def deserialize_json(data: str) -> StepType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepType value: {data!r}")
    return cast(StepType, data)
