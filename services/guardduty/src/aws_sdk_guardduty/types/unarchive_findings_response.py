"""Generated from Smithy shape ``com.amazonaws.guardduty#UnarchiveFindingsResponse``."""

from typing_extensions import TypedDict


class UnarchiveFindingsResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: UnarchiveFindingsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UnarchiveFindingsResponse:
    out: UnarchiveFindingsResponse = {}  # type: ignore[typeddict-item]
    return out
