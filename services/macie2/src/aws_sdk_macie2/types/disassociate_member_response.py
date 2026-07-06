"""Generated from Smithy shape ``com.amazonaws.macie2#DisassociateMemberResponse``."""

from typing_extensions import TypedDict


class DisassociateMemberResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMemberResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMemberResponse:
    out: DisassociateMemberResponse = {}  # type: ignore[typeddict-item]
    return out
