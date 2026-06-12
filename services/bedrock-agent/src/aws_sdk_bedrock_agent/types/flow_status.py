"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

FlowStatus: TypeAlias = Literal[
    "Failed",
    "Prepared",
    "Preparing",
    "NotPrepared",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Failed",
        "Prepared",
        "Preparing",
        "NotPrepared",
    )
)


def serialize_json(value: FlowStatus) -> str:
    return value


def deserialize_json(data: str) -> FlowStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowStatus value: {data!r}")
    return cast(FlowStatus, data)
