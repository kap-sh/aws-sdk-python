"""Generated from Smithy shape ``com.amazonaws.emr#PutManagedScalingPolicyOutput``."""

from typing_extensions import TypedDict


class PutManagedScalingPolicyOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutManagedScalingPolicyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> PutManagedScalingPolicyOutput:
    out: PutManagedScalingPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
