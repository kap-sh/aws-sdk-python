"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamGroupDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_iam_attached_managed_policy_list
    import aws_sdk_securityhub.types.aws_iam_group_policy_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsIamGroupDetails(TypedDict):
    attached_managed_policies: NotRequired[
        "aws_sdk_securityhub.types.aws_iam_attached_managed_policy_list.AwsIamAttachedManagedPolicyList"
    ]
    """<p>A list of the managed policies that are attached to the IAM group.</p>"""
    create_date: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the IAM group was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    group_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the IAM group.</p>"""
    group_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the IAM group.</p>"""
    group_policy_list: NotRequired[
        "aws_sdk_securityhub.types.aws_iam_group_policy_list.AwsIamGroupPolicyList"
    ]
    """<p>The list of inline policies that are embedded in the group.</p>"""
    path: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamGroupDetails) -> dict:
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
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group_policy_list" in value:
        import aws_sdk_securityhub.types.aws_iam_group_policy_list

        out["GroupPolicyList"] = (
            aws_sdk_securityhub.types.aws_iam_group_policy_list.serialize_json(
                value["group_policy_list"]
            )
        )
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_json(data: dict) -> AwsIamGroupDetails:
    out: AwsIamGroupDetails = {}  # type: ignore[typeddict-item]
    if "AttachedManagedPolicies" in data:
        import aws_sdk_securityhub.types.aws_iam_attached_managed_policy_list

        out["attached_managed_policies"] = (
            aws_sdk_securityhub.types.aws_iam_attached_managed_policy_list.deserialize_json(
                data["AttachedManagedPolicies"]
            )
        )
    if "CreateDate" in data:
        out["create_date"] = data["CreateDate"]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "GroupPolicyList" in data:
        import aws_sdk_securityhub.types.aws_iam_group_policy_list

        out["group_policy_list"] = (
            aws_sdk_securityhub.types.aws_iam_group_policy_list.deserialize_json(
                data["GroupPolicyList"]
            )
        )
    if "Path" in data:
        out["path"] = data["Path"]
    return out
