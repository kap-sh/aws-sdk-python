"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DetachManagedPolicyFromPermissionSetResponse``."""

from typing_extensions import TypedDict


class DetachManagedPolicyFromPermissionSetResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachManagedPolicyFromPermissionSetResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DetachManagedPolicyFromPermissionSetResponse:
    out: DetachManagedPolicyFromPermissionSetResponse = {}  # type: ignore[typeddict-item]
    return out
