"""Generated from Smithy shape ``com.amazonaws.deadline#AssociateMemberToQueueResponse``."""

from typing_extensions import TypedDict


class AssociateMemberToQueueResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AssociateMemberToQueueResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateMemberToQueueResponse:
    out: AssociateMemberToQueueResponse = {}  # type: ignore[typeddict-item]
    return out
