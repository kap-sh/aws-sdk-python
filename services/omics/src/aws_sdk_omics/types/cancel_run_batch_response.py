"""Generated from Smithy shape ``com.amazonaws.omics#CancelRunBatchResponse``."""

from typing_extensions import TypedDict


class CancelRunBatchResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelRunBatchResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelRunBatchResponse:
    out: CancelRunBatchResponse = {}  # type: ignore[typeddict-item]
    return out
