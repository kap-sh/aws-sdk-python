"""Generated from Smithy shape ``com.amazonaws.mediastore#PutContainerPolicyOutput``."""

from typing_extensions import TypedDict


class PutContainerPolicyOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutContainerPolicyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> PutContainerPolicyOutput:
    out: PutContainerPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
