"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#Protocol``."""

from typing import Literal, TypeAlias, cast

Protocol: TypeAlias = Literal["WebRTC",]


# --- restJson1 ser/de ---
def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    return cast(Protocol, data)
