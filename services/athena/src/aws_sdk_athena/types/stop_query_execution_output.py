"""Generated from Smithy shape ``com.amazonaws.athena#StopQueryExecutionOutput``."""

from typing import TypedDict


class StopQueryExecutionOutput(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopQueryExecutionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopQueryExecutionOutput:
    out: StopQueryExecutionOutput = {}  # type: ignore[typeddict-item]
    return out
