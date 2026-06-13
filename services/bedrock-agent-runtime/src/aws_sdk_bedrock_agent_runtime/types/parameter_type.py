"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ParameterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

ParameterType: TypeAlias = Literal[
    "string",
    "number",
    "integer",
    "boolean",
    "array",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "string",
        "number",
        "integer",
        "boolean",
        "array",
    )
)


def serialize_json(value: ParameterType) -> str:
    return value


def deserialize_json(data: str) -> ParameterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParameterType value: {data!r}")
    return cast(ParameterType, data)
