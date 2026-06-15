"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

OperatorType: TypeAlias = Literal[
    "EQUALS_TO",
    "EXISTS",
    "NOT_EXISTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS_TO",
        "EXISTS",
        "NOT_EXISTS",
    )
)


def serialize_json(value: OperatorType) -> str:
    return value


def deserialize_json(data: str) -> OperatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperatorType value: {data!r}")
    return cast(OperatorType, data)
