"""Generated from Smithy shape ``com.amazonaws.xray#GetTraceSegmentDestinationRequest``."""

from typing import TypedDict


class GetTraceSegmentDestinationRequest(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetTraceSegmentDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTraceSegmentDestinationRequest:
    out: GetTraceSegmentDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
