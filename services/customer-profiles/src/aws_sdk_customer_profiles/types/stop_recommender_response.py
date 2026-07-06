"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StopRecommenderResponse``."""

from typing_extensions import TypedDict


class StopRecommenderResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopRecommenderResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopRecommenderResponse:
    out: StopRecommenderResponse = {}  # type: ignore[typeddict-item]
    return out
