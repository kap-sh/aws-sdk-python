"""Generated from Smithy shape ``com.amazonaws.notifications#AssociateManagedNotificationAdditionalChannelResponse``."""

from typing_extensions import TypedDict


class AssociateManagedNotificationAdditionalChannelResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(
    value: AssociateManagedNotificationAdditionalChannelResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> AssociateManagedNotificationAdditionalChannelResponse:
    out: AssociateManagedNotificationAdditionalChannelResponse = {}  # type: ignore[typeddict-item]
    return out
