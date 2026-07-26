"""Generated from Smithy shape ``com.amazonaws.frauddetector#CancelBatchPredictionJobResult``."""

from typing_extensions import TypedDict


class CancelBatchPredictionJobResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelBatchPredictionJobResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelBatchPredictionJobResult:
    out: CancelBatchPredictionJobResult = {}  # type: ignore[typeddict-item]
    return out
