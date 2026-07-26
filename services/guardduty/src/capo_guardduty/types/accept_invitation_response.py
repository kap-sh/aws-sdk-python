"""Generated from Smithy shape ``com.amazonaws.guardduty#AcceptInvitationResponse``."""

from typing_extensions import TypedDict


class AcceptInvitationResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AcceptInvitationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AcceptInvitationResponse:
    out: AcceptInvitationResponse = {}  # type: ignore[typeddict-item]
    return out
