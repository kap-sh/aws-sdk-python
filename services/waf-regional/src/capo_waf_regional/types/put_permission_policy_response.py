"""Generated from Smithy shape ``com.amazonaws.wafregional#PutPermissionPolicyResponse``."""

from typing_extensions import TypedDict


class PutPermissionPolicyResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPermissionPolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPermissionPolicyResponse:
    out: PutPermissionPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
