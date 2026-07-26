"""Generated from Smithy shape ``com.amazonaws.emr#RemoveManagedScalingPolicyOutput``."""

from typing_extensions import TypedDict


class RemoveManagedScalingPolicyOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveManagedScalingPolicyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveManagedScalingPolicyOutput:
    out: RemoveManagedScalingPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
