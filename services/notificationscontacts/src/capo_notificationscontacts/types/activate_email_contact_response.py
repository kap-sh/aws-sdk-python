"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#ActivateEmailContactResponse``."""

from typing_extensions import TypedDict


class ActivateEmailContactResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ActivateEmailContactResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ActivateEmailContactResponse:
    out: ActivateEmailContactResponse = {}  # type: ignore[typeddict-item]
    return out
