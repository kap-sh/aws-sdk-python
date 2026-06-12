"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DetachCustomerManagedPolicyReferenceFromPermissionSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.customer_managed_policy_reference
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.permission_set_arn


class DetachCustomerManagedPolicyReferenceFromPermissionSetRequest(TypedDict):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>"""
    permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the <code>PermissionSet</code>.</p>"""
    customer_managed_policy_reference: "aws_sdk_sso_admin.types.customer_managed_policy_reference.CustomerManagedPolicyReference"
    """<p>Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each Amazon Web Services account where you want to deploy your permission set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DetachCustomerManagedPolicyReferenceFromPermissionSetRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    import aws_sdk_sso_admin.types.customer_managed_policy_reference

    out["CustomerManagedPolicyReference"] = (
        aws_sdk_sso_admin.types.customer_managed_policy_reference.serialize_aws_json_1_1(
            value["customer_managed_policy_reference"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DetachCustomerManagedPolicyReferenceFromPermissionSetRequest:
    out: DetachCustomerManagedPolicyReferenceFromPermissionSetRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "DetachCustomerManagedPolicyReferenceFromPermissionSetRequest.instance_arn required"
        )
    if "PermissionSetArn" in data:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "DetachCustomerManagedPolicyReferenceFromPermissionSetRequest.permission_set_arn required"
        )
    if "CustomerManagedPolicyReference" in data:
        import aws_sdk_sso_admin.types.customer_managed_policy_reference

        out["customer_managed_policy_reference"] = (
            aws_sdk_sso_admin.types.customer_managed_policy_reference.deserialize_aws_json_1_1(
                data["CustomerManagedPolicyReference"]
            )
        )
    else:
        raise DeserializationError(
            "DetachCustomerManagedPolicyReferenceFromPermissionSetRequest.customer_managed_policy_reference required"
        )
    return out
