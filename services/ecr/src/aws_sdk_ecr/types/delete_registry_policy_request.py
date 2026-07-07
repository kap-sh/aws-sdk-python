"""Generated from Smithy shape ``com.amazonaws.ecr#DeleteRegistryPolicyRequest``."""

from typing_extensions import TypedDict


class DeleteRegistryPolicyRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRegistryPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRegistryPolicyRequest:
    out: DeleteRegistryPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
