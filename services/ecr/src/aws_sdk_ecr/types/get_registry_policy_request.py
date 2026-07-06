"""Generated from Smithy shape ``com.amazonaws.ecr#GetRegistryPolicyRequest``."""

from typing_extensions import TypedDict


class GetRegistryPolicyRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegistryPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegistryPolicyRequest:
    out: GetRegistryPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
