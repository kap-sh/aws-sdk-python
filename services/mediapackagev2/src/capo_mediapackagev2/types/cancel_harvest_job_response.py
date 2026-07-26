"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CancelHarvestJobResponse``."""

from typing_extensions import TypedDict


class CancelHarvestJobResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelHarvestJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelHarvestJobResponse:
    out: CancelHarvestJobResponse = {}  # type: ignore[typeddict-item]
    return out
