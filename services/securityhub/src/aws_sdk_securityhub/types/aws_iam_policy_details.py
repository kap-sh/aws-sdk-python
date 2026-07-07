"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamPolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_iam_policy_version_list
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsIamPolicyDetails(TypedDict, closed=True):
    attachment_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of users, groups, and roles that the policy is attached to.</p>"""
    create_date: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>When the policy was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    default_version_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the default version of the policy.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A description of the policy.</p>"""
    is_attachable: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the policy can be attached to a user, group, or role.</p>"""
    path: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the policy.</p>"""
    permissions_boundary_usage_count: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>The number of users and roles that use the policy to set the permissions boundary.</p>"""
    policy_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier of the policy.</p>"""
    policy_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the policy.</p>"""
    policy_version_list: NotRequired[
        "aws_sdk_securityhub.types.aws_iam_policy_version_list.AwsIamPolicyVersionList"
    ]
    """<p>List of versions of the policy.</p>"""
    update_date: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>When the policy was most recently updated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamPolicyDetails) -> dict:
    out: dict = {}
    if "attachment_count" in value:
        out["AttachmentCount"] = value["attachment_count"]
    if "create_date" in value:
        out["CreateDate"] = value["create_date"]
    if "default_version_id" in value:
        out["DefaultVersionId"] = value["default_version_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "is_attachable" in value:
        out["IsAttachable"] = value["is_attachable"]
    if "path" in value:
        out["Path"] = value["path"]
    if "permissions_boundary_usage_count" in value:
        out["PermissionsBoundaryUsageCount"] = value["permissions_boundary_usage_count"]
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "policy_version_list" in value:
        import aws_sdk_securityhub.types.aws_iam_policy_version_list

        out["PolicyVersionList"] = (
            aws_sdk_securityhub.types.aws_iam_policy_version_list.serialize_json(
                value["policy_version_list"]
            )
        )
    if "update_date" in value:
        out["UpdateDate"] = value["update_date"]
    return out


def deserialize_json(data: dict) -> AwsIamPolicyDetails:
    out: AwsIamPolicyDetails = {}  # type: ignore[typeddict-item]
    if "AttachmentCount" in data:
        out["attachment_count"] = data["AttachmentCount"]
    if "CreateDate" in data:
        out["create_date"] = data["CreateDate"]
    if "DefaultVersionId" in data:
        out["default_version_id"] = data["DefaultVersionId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "IsAttachable" in data:
        out["is_attachable"] = data["IsAttachable"]
    if "Path" in data:
        out["path"] = data["Path"]
    if "PermissionsBoundaryUsageCount" in data:
        out["permissions_boundary_usage_count"] = data["PermissionsBoundaryUsageCount"]
    if "PolicyId" in data:
        out["policy_id"] = data["PolicyId"]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    if "PolicyVersionList" in data:
        import aws_sdk_securityhub.types.aws_iam_policy_version_list

        out["policy_version_list"] = (
            aws_sdk_securityhub.types.aws_iam_policy_version_list.deserialize_json(
                data["PolicyVersionList"]
            )
        )
    if "UpdateDate" in data:
        out["update_date"] = data["UpdateDate"]
    return out
