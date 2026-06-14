"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SchemaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

SchemaType: TypeAlias = Literal[
    "string",
    "number",
    "object",
    "array",
    "boolean",
    "integer",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "string",
        "number",
        "object",
        "array",
        "boolean",
        "integer",
    )
)


def serialize_json(value: SchemaType) -> str:
    return value


def deserialize_json(data: str) -> SchemaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaType value: {data!r}")
    return cast(SchemaType, data)
