"""Generated from Smithy shape ``com.amazonaws.deadline#DisassociateMemberFromQueueResponse``."""

from typing_extensions import TypedDict


class DisassociateMemberFromQueueResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMemberFromQueueResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMemberFromQueueResponse:
    out: DisassociateMemberFromQueueResponse = {}  # type: ignore[typeddict-item]
    return out
