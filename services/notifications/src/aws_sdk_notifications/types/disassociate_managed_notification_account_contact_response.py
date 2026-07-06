"""Generated from Smithy shape ``com.amazonaws.notifications#DisassociateManagedNotificationAccountContactResponse``."""

from typing_extensions import TypedDict


class DisassociateManagedNotificationAccountContactResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(
    value: DisassociateManagedNotificationAccountContactResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> DisassociateManagedNotificationAccountContactResponse:
    out: DisassociateManagedNotificationAccountContactResponse = {}  # type: ignore[typeddict-item]
    return out
