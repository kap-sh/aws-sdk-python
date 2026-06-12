"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopJobResponse``."""

from typing import TypedDict


class StopJobResponse(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopJobResponse:
    out: StopJobResponse = {}  # type: ignore[typeddict-item]
    return out
