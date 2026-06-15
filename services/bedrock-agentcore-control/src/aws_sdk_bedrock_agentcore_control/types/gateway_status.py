"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

GatewayStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "UPDATE_UNSUCCESSFUL",
    "DELETING",
    "READY",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "UPDATE_UNSUCCESSFUL",
        "DELETING",
        "READY",
        "FAILED",
    )
)


def serialize_json(value: GatewayStatus) -> str:
    return value


def deserialize_json(data: str) -> GatewayStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayStatus value: {data!r}")
    return cast(GatewayStatus, data)
