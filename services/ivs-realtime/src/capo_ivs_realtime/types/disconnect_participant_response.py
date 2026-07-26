"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DisconnectParticipantResponse``."""

from typing_extensions import TypedDict


class DisconnectParticipantResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectParticipantResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisconnectParticipantResponse:
    out: DisconnectParticipantResponse = {}  # type: ignore[typeddict-item]
    return out
