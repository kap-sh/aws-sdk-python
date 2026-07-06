"""Generated from Smithy shape ``com.amazonaws.emr#RemoveAutoTerminationPolicyOutput``."""

from typing_extensions import TypedDict


class RemoveAutoTerminationPolicyOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveAutoTerminationPolicyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveAutoTerminationPolicyOutput:
    out: RemoveAutoTerminationPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
