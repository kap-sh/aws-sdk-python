"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentConnectorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

PaymentConnectorStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "READY",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "DELETING",
        "READY",
        "CREATE_FAILED",
        "UPDATE_FAILED",
        "DELETE_FAILED",
    )
)


def serialize_json(value: PaymentConnectorStatus) -> str:
    return value


def deserialize_json(data: str) -> PaymentConnectorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentConnectorStatus value: {data!r}")
    return cast(PaymentConnectorStatus, data)
