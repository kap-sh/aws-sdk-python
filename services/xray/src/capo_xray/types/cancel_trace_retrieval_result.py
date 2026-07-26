"""Generated from Smithy shape ``com.amazonaws.xray#CancelTraceRetrievalResult``."""

from typing_extensions import TypedDict


class CancelTraceRetrievalResult(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelTraceRetrievalResult) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelTraceRetrievalResult:
    out: CancelTraceRetrievalResult = {}  # type: ignore[typeddict-item]
    return out
