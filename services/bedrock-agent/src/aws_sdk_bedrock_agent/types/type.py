"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

Type: TypeAlias = Literal[
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


def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)
