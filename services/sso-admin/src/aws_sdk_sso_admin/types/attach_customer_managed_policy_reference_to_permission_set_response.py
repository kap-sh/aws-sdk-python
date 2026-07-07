"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AttachCustomerManagedPolicyReferenceToPermissionSetResponse``."""

from typing_extensions import TypedDict


class AttachCustomerManagedPolicyReferenceToPermissionSetResponse(
    TypedDict, closed=True
):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AttachCustomerManagedPolicyReferenceToPermissionSetResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AttachCustomerManagedPolicyReferenceToPermissionSetResponse:
    out: AttachCustomerManagedPolicyReferenceToPermissionSetResponse = {}  # type: ignore[typeddict-item]
    return out
