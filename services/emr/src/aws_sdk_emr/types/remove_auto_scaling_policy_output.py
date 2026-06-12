"""Generated from Smithy shape ``com.amazonaws.emr#RemoveAutoScalingPolicyOutput``."""

from typing import TypedDict


class RemoveAutoScalingPolicyOutput(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveAutoScalingPolicyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveAutoScalingPolicyOutput:
    out: RemoveAutoScalingPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
