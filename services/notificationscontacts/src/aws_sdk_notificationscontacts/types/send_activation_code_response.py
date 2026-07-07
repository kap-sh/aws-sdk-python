"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#SendActivationCodeResponse``."""

from typing_extensions import TypedDict


class SendActivationCodeResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendActivationCodeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendActivationCodeResponse:
    out: SendActivationCodeResponse = {}  # type: ignore[typeddict-item]
    return out
