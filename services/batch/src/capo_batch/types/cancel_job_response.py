"""Generated from Smithy shape ``com.amazonaws.batch#CancelJobResponse``."""

from typing_extensions import TypedDict


class CancelJobResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelJobResponse:
    out: CancelJobResponse = {}  # type: ignore[typeddict-item]
    return out
