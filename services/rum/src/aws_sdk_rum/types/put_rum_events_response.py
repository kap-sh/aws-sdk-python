"""Generated from Smithy shape ``com.amazonaws.rum#PutRumEventsResponse``."""

from typing_extensions import TypedDict


class PutRumEventsResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutRumEventsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutRumEventsResponse:
    out: PutRumEventsResponse = {}  # type: ignore[typeddict-item]
    return out
