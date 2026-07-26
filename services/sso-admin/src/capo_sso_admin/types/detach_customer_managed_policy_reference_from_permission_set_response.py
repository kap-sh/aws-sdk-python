"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DetachCustomerManagedPolicyReferenceFromPermissionSetResponse``."""

from typing_extensions import TypedDict


class DetachCustomerManagedPolicyReferenceFromPermissionSetResponse(
    TypedDict, closed=True
):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DetachCustomerManagedPolicyReferenceFromPermissionSetResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DetachCustomerManagedPolicyReferenceFromPermissionSetResponse:
    out: DetachCustomerManagedPolicyReferenceFromPermissionSetResponse = {}  # type: ignore[typeddict-item]
    return out
