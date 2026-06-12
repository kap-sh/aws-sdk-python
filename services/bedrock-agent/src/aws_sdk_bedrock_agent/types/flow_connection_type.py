"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowConnectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

FlowConnectionType: TypeAlias = Literal[
    "Data",
    "Conditional",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Data",
        "Conditional",
    )
)


def serialize_json(value: FlowConnectionType) -> str:
    return value


def deserialize_json(data: str) -> FlowConnectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowConnectionType value: {data!r}")
    return cast(FlowConnectionType, data)
