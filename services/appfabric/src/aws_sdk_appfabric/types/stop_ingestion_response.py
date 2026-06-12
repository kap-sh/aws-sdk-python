"""Generated from Smithy shape ``com.amazonaws.appfabric#StopIngestionResponse``."""

from typing import TypedDict


class StopIngestionResponse(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopIngestionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopIngestionResponse:
    out: StopIngestionResponse = {}  # type: ignore[typeddict-item]
    return out
