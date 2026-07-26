"""Generated from Smithy shape ``com.amazonaws.m2#CancelBatchJobExecutionResponse``."""

from typing_extensions import TypedDict


class CancelBatchJobExecutionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelBatchJobExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelBatchJobExecutionResponse:
    out: CancelBatchJobExecutionResponse = {}  # type: ignore[typeddict-item]
    return out
