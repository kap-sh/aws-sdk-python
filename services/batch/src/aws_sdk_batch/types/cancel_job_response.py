"""Generated from Smithy shape ``com.amazonaws.batch#CancelJobResponse``."""

from typing import TypedDict


class CancelJobResponse(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelJobResponse:
    out: CancelJobResponse = {}  # type: ignore[typeddict-item]
    return out
