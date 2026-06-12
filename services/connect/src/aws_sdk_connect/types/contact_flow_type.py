"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactFlowType: TypeAlias = Literal[
    "CONTACT_FLOW",
    "CUSTOMER_QUEUE",
    "CUSTOMER_HOLD",
    "CUSTOMER_WHISPER",
    "AGENT_HOLD",
    "AGENT_WHISPER",
    "OUTBOUND_WHISPER",
    "AGENT_TRANSFER",
    "QUEUE_TRANSFER",
    "CAMPAIGN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTACT_FLOW",
        "CUSTOMER_QUEUE",
        "CUSTOMER_HOLD",
        "CUSTOMER_WHISPER",
        "AGENT_HOLD",
        "AGENT_WHISPER",
        "OUTBOUND_WHISPER",
        "AGENT_TRANSFER",
        "QUEUE_TRANSFER",
        "CAMPAIGN",
    )
)


def serialize_json(value: ContactFlowType) -> str:
    return value


def deserialize_json(data: str) -> ContactFlowType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactFlowType value: {data!r}")
    return cast(ContactFlowType, data)
