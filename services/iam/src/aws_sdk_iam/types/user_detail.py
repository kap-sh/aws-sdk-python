"""Generated from Smithy shape ``com.amazonaws.iam#UserDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.attached_permissions_boundary
    import aws_sdk_iam.types.attached_policies_list_type
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.group_name_list_type
    import aws_sdk_iam.types.id_type
    import aws_sdk_iam.types.path_type
    import aws_sdk_iam.types.policy_detail_list_type
    import aws_sdk_iam.types.tag_list_type
    import aws_sdk_iam.types.user_name_type


class UserDetail(TypedDict):
    path: NotRequired["aws_sdk_iam.types.path_type.pathType"]
    r"""<p>The path to the user. For more information about paths, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    user_name: NotRequired["aws_sdk_iam.types.user_name_type.userNameType"]
    """<p>The friendly name identifying the user.</p>"""
    user_id: NotRequired["aws_sdk_iam.types.id_type.idType"]
    r"""<p>The stable and unique string identifying the user. For more information about IDs, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    arn: NotRequired["aws_sdk_iam.types.arn_type.arnType"]
    create_date: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    r"""<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the user was created.</p>"""
    user_policy_list: NotRequired[
        "aws_sdk_iam.types.policy_detail_list_type.policyDetailListType"
    ]
    """<p>A list of the inline policies embedded in the user.</p>"""
    group_list: NotRequired["aws_sdk_iam.types.group_name_list_type.groupNameListType"]
    """<p>A list of IAM groups that the user is in.</p>"""
    attached_managed_policies: NotRequired[
        "aws_sdk_iam.types.attached_policies_list_type.attachedPoliciesListType"
    ]
    """<p>A list of the managed policies attached to the user.</p>"""
    permissions_boundary: NotRequired[
        "aws_sdk_iam.types.attached_permissions_boundary.AttachedPermissionsBoundary"
    ]
    r"""<p>The ARN of the policy used to set the permissions boundary for the user.</p> <p>For more information about permissions boundaries, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html\">Permissions boundaries for IAM identities </a> in the <i>IAM User Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_iam.types.tag_list_type.tagListType"]
    r"""<p>A list of tags that are associated with the user. For more information about tagging, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html\">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UserDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "path" in value:
        pairs.append((f"{prefix}.Path", str(value["path"])))
    if "user_name" in value:
        pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    if "user_id" in value:
        pairs.append((f"{prefix}.UserId", str(value["user_id"])))
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "create_date" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "user_policy_list" in value:
        import aws_sdk_iam.types.policy_detail_list_type

        aws_sdk_iam.types.policy_detail_list_type.serialize_query(
            value["user_policy_list"], pairs, f"{prefix}.UserPolicyList"
        )
    if "group_list" in value:
        import aws_sdk_iam.types.group_name_list_type

        aws_sdk_iam.types.group_name_list_type.serialize_query(
            value["group_list"], pairs, f"{prefix}.GroupList"
        )
    if "attached_managed_policies" in value:
        import aws_sdk_iam.types.attached_policies_list_type

        aws_sdk_iam.types.attached_policies_list_type.serialize_query(
            value["attached_managed_policies"],
            pairs,
            f"{prefix}.AttachedManagedPolicies",
        )
    if "permissions_boundary" in value:
        import aws_sdk_iam.types.attached_permissions_boundary

        aws_sdk_iam.types.attached_permissions_boundary.serialize_query(
            value["permissions_boundary"], pairs, f"{prefix}.PermissionsBoundary"
        )
    if "tags" in value:
        import aws_sdk_iam.types.tag_list_type

        aws_sdk_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> UserDetail:
    out: UserDetail = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_iam.types.date_type

        out["create_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_create_date
        )
    child_user_policy_list = el.find("UserPolicyList")
    if child_user_policy_list is not None:
        import aws_sdk_iam.types.policy_detail_list_type

        out["user_policy_list"] = (
            aws_sdk_iam.types.policy_detail_list_type.deserialize_query(
                child_user_policy_list
            )
        )
    child_group_list = el.find("GroupList")
    if child_group_list is not None:
        import aws_sdk_iam.types.group_name_list_type

        out["group_list"] = aws_sdk_iam.types.group_name_list_type.deserialize_query(
            child_group_list
        )
    child_attached_managed_policies = el.find("AttachedManagedPolicies")
    if child_attached_managed_policies is not None:
        import aws_sdk_iam.types.attached_policies_list_type

        out["attached_managed_policies"] = (
            aws_sdk_iam.types.attached_policies_list_type.deserialize_query(
                child_attached_managed_policies
            )
        )
    child_permissions_boundary = el.find("PermissionsBoundary")
    if child_permissions_boundary is not None:
        import aws_sdk_iam.types.attached_permissions_boundary

        out["permissions_boundary"] = (
            aws_sdk_iam.types.attached_permissions_boundary.deserialize_query(
                child_permissions_boundary
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
