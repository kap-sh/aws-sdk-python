"""Generated from Smithy shape ``com.amazonaws.emr#PutAutoTerminationPolicyOutput``."""

from typing import TypedDict


class PutAutoTerminationPolicyOutput(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAutoTerminationPolicyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAutoTerminationPolicyOutput:
    out: PutAutoTerminationPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
