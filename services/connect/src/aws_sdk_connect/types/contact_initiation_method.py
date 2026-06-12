"""Generated from Smithy shape ``com.amazonaws.connect#ContactInitiationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactInitiationMethod: TypeAlias = Literal[
    "INBOUND",
    "OUTBOUND",
    "TRANSFER",
    "QUEUE_TRANSFER",
    "CALLBACK",
    "API",
    "DISCONNECT",
    "MONITOR",
    "EXTERNAL_OUTBOUND",
    "WEBRTC_API",
    "AGENT_REPLY",
    "FLOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INBOUND",
        "OUTBOUND",
        "TRANSFER",
        "QUEUE_TRANSFER",
        "CALLBACK",
        "API",
        "DISCONNECT",
        "MONITOR",
        "EXTERNAL_OUTBOUND",
        "WEBRTC_API",
        "AGENT_REPLY",
        "FLOW",
    )
)


def serialize_json(value: ContactInitiationMethod) -> str:
    return value


def deserialize_json(data: str) -> ContactInitiationMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactInitiationMethod value: {data!r}")
    return cast(ContactInitiationMethod, data)
