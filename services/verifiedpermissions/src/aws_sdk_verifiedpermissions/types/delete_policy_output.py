"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeletePolicyOutput``."""

from typing_extensions import TypedDict


class DeletePolicyOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePolicyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePolicyOutput:
    out: DeletePolicyOutput = {}  # type: ignore[typeddict-item]
    return out
