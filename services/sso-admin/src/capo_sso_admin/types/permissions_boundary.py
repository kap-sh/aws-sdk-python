"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PermissionsBoundary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.customer_managed_policy_reference
    import capo_sso_admin.types.managed_policy_arn


class PermissionsBoundary(TypedDict, closed=True):
    customer_managed_policy_reference: NotRequired[
        "capo_sso_admin.types.customer_managed_policy_reference.CustomerManagedPolicyReference"
    ]
    """<p>Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each Amazon Web Services account where you want to deploy your permission set.</p>"""
    managed_policy_arn: NotRequired[
        "capo_sso_admin.types.managed_policy_arn.ManagedPolicyArn"
    ]
    """<p>The Amazon Web Services managed policy ARN that you want to attach to a permission set as a permissions boundary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionsBoundary) -> dict:
    out: dict = {}
    if "customer_managed_policy_reference" in value:
        import capo_sso_admin.types.customer_managed_policy_reference

        out["CustomerManagedPolicyReference"] = (
            capo_sso_admin.types.customer_managed_policy_reference.serialize_aws_json_1_1(
                value["customer_managed_policy_reference"]
            )
        )
    if "managed_policy_arn" in value:
        out["ManagedPolicyArn"] = value["managed_policy_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PermissionsBoundary:
    out: PermissionsBoundary = {}  # type: ignore[typeddict-item]
    if "CustomerManagedPolicyReference" in data:
        import capo_sso_admin.types.customer_managed_policy_reference

        out["customer_managed_policy_reference"] = (
            capo_sso_admin.types.customer_managed_policy_reference.deserialize_aws_json_1_1(
                data["CustomerManagedPolicyReference"]
            )
        )
    if "ManagedPolicyArn" in data:
        out["managed_policy_arn"] = data["ManagedPolicyArn"]
    return out
