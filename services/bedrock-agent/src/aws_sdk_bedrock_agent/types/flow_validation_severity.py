"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowValidationSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

FlowValidationSeverity: TypeAlias = Literal[
    "Warning",
    "Error",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Warning",
        "Error",
    )
)


def serialize_json(value: FlowValidationSeverity) -> str:
    return value


def deserialize_json(data: str) -> FlowValidationSeverity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowValidationSeverity value: {data!r}")
    return cast(FlowValidationSeverity, data)
