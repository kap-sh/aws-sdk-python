"""Generated from Smithy shape ``com.amazonaws.connect#ContactInitiationMethod``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ContactInitiationMethod) -> str:
    return value


def deserialize_json(data: str) -> ContactInitiationMethod:
    return cast(ContactInitiationMethod, data)
