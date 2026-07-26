"""Generated from Smithy shape ``com.amazonaws.connect#OutboundMessageSourceType``."""

from typing import Literal, TypeAlias, cast

OutboundMessageSourceType: TypeAlias = Literal[
    "TEMPLATE",
    "RAW",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutboundMessageSourceType) -> str:
    return value


def deserialize_json(data: str) -> OutboundMessageSourceType:
    return cast(OutboundMessageSourceType, data)
