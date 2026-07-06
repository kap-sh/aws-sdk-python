"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#DeleteEmailContactResponse``."""

from typing_extensions import TypedDict


class DeleteEmailContactResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEmailContactResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEmailContactResponse:
    out: DeleteEmailContactResponse = {}  # type: ignore[typeddict-item]
    return out
