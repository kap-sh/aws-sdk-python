"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ExecutionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

ExecutionType: TypeAlias = Literal[
    "LAMBDA",
    "RETURN_CONTROL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LAMBDA",
        "RETURN_CONTROL",
    )
)


def serialize_json(value: ExecutionType) -> str:
    return value


def deserialize_json(data: str) -> ExecutionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionType value: {data!r}")
    return cast(ExecutionType, data)
