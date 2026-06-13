"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputQueryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

InputQueryType: TypeAlias = Literal["TEXT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TEXT",))


def serialize_json(value: InputQueryType) -> str:
    return value


def deserialize_json(data: str) -> InputQueryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputQueryType value: {data!r}")
    return cast(InputQueryType, data)
