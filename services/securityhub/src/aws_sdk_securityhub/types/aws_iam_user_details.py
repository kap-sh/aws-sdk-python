"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamUserDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_iam_attached_managed_policy_list
    import aws_sdk_securityhub.types.aws_iam_permissions_boundary
    import aws_sdk_securityhub.types.aws_iam_user_policy_list
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class AwsIamUserDetails(TypedDict):
    attached_managed_policies: NotRequired[
        "aws_sdk_securityhub.types.aws_iam_attached_managed_policy_list.AwsIamAttachedManagedPolicyList"
    ]
    """<p>A list of the managed policies that are attached to the user.</p>"""
    create_date: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the user was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    group_list: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>A list of IAM groups that the user belongs to.</p>"""
    path: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the user.</p>"""
    permissions_boundary: NotRequired[
        "aws_sdk_securityhub.types.aws_iam_permissions_boundary.AwsIamPermissionsBoundary"
    ]
    """<p>The permissions boundary for the user.</p>"""
    user_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier for the user.</p>"""
    user_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the user.</p>"""
    user_policy_list: NotRequired[
        "aws_sdk_securityhub.types.aws_iam_user_policy_list.AwsIamUserPolicyList"
    ]
    """<p>The list of inline policies that are embedded in the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamUserDetails) -> dict:
    out: dict = {}
    if "attached_managed_policies" in value:
        import aws_sdk_securityhub.types.aws_iam_attached_managed_policy_list

        out["AttachedManagedPolicies"] = (
            aws_sdk_securityhub.types.aws_iam_attached_managed_policy_list.serialize_json(
                value["attached_managed_policies"]
            )
        )
    if "create_date" in value:
        out["CreateDate"] = value["create_date"]
    if "group_list" in value:
        import aws_sdk_securityhub.types.string_list

        out["GroupList"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["group_list"]
        )
    if "path" in value:
        out["Path"] = value["path"]
    if "permissions_boundary" in value:
        import aws_sdk_securityhub.types.aws_iam_permissions_boundary

        out["PermissionsBoundary"] = (
            aws_sdk_securityhub.types.aws_iam_permissions_boundary.serialize_json(
                value["permissions_boundary"]
            )
        )
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "user_policy_list" in value:
        import aws_sdk_securityhub.types.aws_iam_user_policy_list

        out["UserPolicyList"] = (
            aws_sdk_securityhub.types.aws_iam_user_policy_list.serialize_json(
                value["user_policy_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsIamUserDetails:
    out: AwsIamUserDetails = {}  # type: ignore[typeddict-item]
    if "AttachedManagedPolicies" in data:
        import aws_sdk_securityhub.types.aws_iam_attached_managed_policy_list

        out["attached_managed_policies"] = (
            aws_sdk_securityhub.types.aws_iam_attached_managed_policy_list.deserialize_json(
                data["AttachedManagedPolicies"]
            )
        )
    if "CreateDate" in data:
        out["create_date"] = data["CreateDate"]
    if "GroupList" in data:
        import aws_sdk_securityhub.types.string_list

        out["group_list"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["GroupList"]
        )
    if "Path" in data:
        out["path"] = data["Path"]
    if "PermissionsBoundary" in data:
        import aws_sdk_securityhub.types.aws_iam_permissions_boundary

        out["permissions_boundary"] = (
            aws_sdk_securityhub.types.aws_iam_permissions_boundary.deserialize_json(
                data["PermissionsBoundary"]
            )
        )
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "UserPolicyList" in data:
        import aws_sdk_securityhub.types.aws_iam_user_policy_list

        out["user_policy_list"] = (
            aws_sdk_securityhub.types.aws_iam_user_policy_list.deserialize_json(
                data["UserPolicyList"]
            )
        )
    return out
