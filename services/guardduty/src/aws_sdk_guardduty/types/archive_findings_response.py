"""Generated from Smithy shape ``com.amazonaws.guardduty#ArchiveFindingsResponse``."""

from typing_extensions import TypedDict


class ArchiveFindingsResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveFindingsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ArchiveFindingsResponse:
    out: ArchiveFindingsResponse = {}  # type: ignore[typeddict-item]
    return out
