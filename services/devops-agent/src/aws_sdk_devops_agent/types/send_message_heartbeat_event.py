"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageHeartbeatEvent``."""

from typing import TypedDict


class SendMessageHeartbeatEvent(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageHeartbeatEvent) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendMessageHeartbeatEvent:
    out: SendMessageHeartbeatEvent = {}  # type: ignore[typeddict-item]
    return out
