"""Generated from Smithy shape ``com.amazonaws.devopsguru#RemoveNotificationChannelResponse``."""

from typing_extensions import TypedDict


class RemoveNotificationChannelResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RemoveNotificationChannelResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveNotificationChannelResponse:
    out: RemoveNotificationChannelResponse = {}  # type: ignore[typeddict-item]
    return out
