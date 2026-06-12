"""Generated from Smithy shape ``com.amazonaws.sfn#SendTaskSuccessOutput``."""

from typing import TypedDict


class SendTaskSuccessOutput(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendTaskSuccessOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> SendTaskSuccessOutput:
    out: SendTaskSuccessOutput = {}  # type: ignore[typeddict-item]
    return out
