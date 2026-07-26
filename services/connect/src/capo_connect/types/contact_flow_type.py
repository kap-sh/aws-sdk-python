"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ContactFlowType) -> str:
    return value


def deserialize_json(data: str) -> ContactFlowType:
    return cast(ContactFlowType, data)
