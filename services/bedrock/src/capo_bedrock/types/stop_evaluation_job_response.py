"""Generated from Smithy shape ``com.amazonaws.bedrock#StopEvaluationJobResponse``."""

from typing_extensions import TypedDict


class StopEvaluationJobResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopEvaluationJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopEvaluationJobResponse:
    out: StopEvaluationJobResponse = {}  # type: ignore[typeddict-item]
    return out
