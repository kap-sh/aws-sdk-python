"""Generated from Smithy shape ``com.amazonaws.securityhub#DisassociateMembersResponse``."""

from typing_extensions import TypedDict


class DisassociateMembersResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMembersResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMembersResponse:
    out: DisassociateMembersResponse = {}  # type: ignore[typeddict-item]
    return out
