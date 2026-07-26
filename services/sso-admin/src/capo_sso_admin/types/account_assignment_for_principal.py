"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccountAssignmentForPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.account_id
    import capo_sso_admin.types.permission_set_arn
    import capo_sso_admin.types.principal_id
    import capo_sso_admin.types.principal_type


class AccountAssignmentForPrincipal(TypedDict, closed=True):
    account_id: NotRequired["capo_sso_admin.types.account_id.AccountId"]
    """<p>The account ID number of the Amazon Web Services account.</p>"""
    permission_set_arn: NotRequired[
        "capo_sso_admin.types.permission_set_arn.PermissionSetArn"
    ]
    """<p>The ARN of the IAM Identity Center permission set assigned to this principal for this Amazon Web Services account.</p>"""
    principal_id: NotRequired["capo_sso_admin.types.principal_id.PrincipalId"]
    """<p>The ID of the principal.</p>"""
    principal_type: NotRequired["capo_sso_admin.types.principal_type.PrincipalType"]
    """<p>The type of the principal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountAssignmentForPrincipal) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "permission_set_arn" in value:
        out["PermissionSetArn"] = value["permission_set_arn"]
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "principal_type" in value:
        import capo_sso_admin.types.principal_type

        out["PrincipalType"] = (
            capo_sso_admin.types.principal_type.serialize_aws_json_1_1(
                value["principal_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountAssignmentForPrincipal:
    out: AccountAssignmentForPrincipal = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "PermissionSetArn" in data:
        out["permission_set_arn"] = data["PermissionSetArn"]
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    if "PrincipalType" in data:
        import capo_sso_admin.types.principal_type

        out["principal_type"] = (
            capo_sso_admin.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    return out
