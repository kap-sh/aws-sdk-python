"""Generated from Smithy shape ``com.amazonaws.sfn#SendTaskFailureOutput``."""

from typing import TypedDict


class SendTaskFailureOutput(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendTaskFailureOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> SendTaskFailureOutput:
    out: SendTaskFailureOutput = {}  # type: ignore[typeddict-item]
    return out
