"""Generated from Smithy shape ``com.amazonaws.cognitosync#UnsubscribeFromDatasetResponse``."""

from typing_extensions import TypedDict


class UnsubscribeFromDatasetResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: UnsubscribeFromDatasetResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UnsubscribeFromDatasetResponse:
    out: UnsubscribeFromDatasetResponse = {}  # type: ignore[typeddict-item]
    return out
