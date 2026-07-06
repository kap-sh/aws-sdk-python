"""Generated from Smithy shape ``com.amazonaws.connectparticipant#CancelParticipantAuthenticationResponse``."""

from typing_extensions import TypedDict


class CancelParticipantAuthenticationResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelParticipantAuthenticationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelParticipantAuthenticationResponse:
    out: CancelParticipantAuthenticationResponse = {}  # type: ignore[typeddict-item]
    return out
