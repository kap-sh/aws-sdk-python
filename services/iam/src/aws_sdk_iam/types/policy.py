"""Generated from Smithy shape ``com.amazonaws.iam#Policy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.attachment_count_type
    import aws_sdk_iam.types.boolean_type
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.id_type
    import aws_sdk_iam.types.policy_description_type
    import aws_sdk_iam.types.policy_name_type
    import aws_sdk_iam.types.policy_path_type
    import aws_sdk_iam.types.policy_version_id_type
    import aws_sdk_iam.types.tag_list_type


class Policy(TypedDict, closed=True):
    policy_name: NotRequired["aws_sdk_iam.types.policy_name_type.policyNameType"]
    """<p>The friendly name (not ARN) identifying the policy.</p>"""
    policy_id: NotRequired["aws_sdk_iam.types.id_type.idType"]
    r"""<p>The stable and unique string identifying the policy.</p> <p>For more information about IDs, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    arn: NotRequired["aws_sdk_iam.types.arn_type.arnType"]
    path: NotRequired["aws_sdk_iam.types.policy_path_type.policyPathType"]
    r"""<p>The path to the policy.</p> <p>For more information about paths, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    default_version_id: NotRequired[
        "aws_sdk_iam.types.policy_version_id_type.policyVersionIdType"
    ]
    """<p>The identifier for the version of the policy that is set as the default version.</p>"""
    attachment_count: NotRequired[
        "aws_sdk_iam.types.attachment_count_type.attachmentCountType"
    ]
    """<p>The number of entities (users, groups, and roles) that the policy is attached to.</p>"""
    permissions_boundary_usage_count: NotRequired[
        "aws_sdk_iam.types.attachment_count_type.attachmentCountType"
    ]
    r"""<p>The number of entities (users and roles) for which the policy is used to set the permissions boundary. </p> <p>For more information about permissions boundaries, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html\">Permissions boundaries for IAM identities </a> in the <i>IAM User Guide</i>.</p>"""
    is_attachable: "aws_sdk_iam.types.boolean_type.booleanType"
    """<p>Specifies whether the policy can be attached to an IAM user, group, or role.</p>"""
    description: NotRequired[
        "aws_sdk_iam.types.policy_description_type.policyDescriptionType"
    ]
    r"""<p>A friendly description of the policy.</p> <p>This element is included in the response to the <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicy.html\">GetPolicy</a> operation. It is not included in the response to the <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicies.html\">ListPolicies</a> operation. </p>"""
    create_date: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    r"""<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the policy was created.</p>"""
    update_date: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    r"""<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the policy was last updated.</p> <p>When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.</p>"""
    tags: NotRequired["aws_sdk_iam.types.tag_list_type.tagListType"]
    r"""<p>A list of tags that are attached to the instance profile. For more information about tagging, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html\">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Policy, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "policy_name" in value:
        pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    if "policy_id" in value:
        pairs.append((f"{prefix}.PolicyId", str(value["policy_id"])))
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "path" in value:
        pairs.append((f"{prefix}.Path", str(value["path"])))
    if "default_version_id" in value:
        pairs.append((f"{prefix}.DefaultVersionId", str(value["default_version_id"])))
    if "attachment_count" in value:
        pairs.append((f"{prefix}.AttachmentCount", str(value["attachment_count"])))
    if "permissions_boundary_usage_count" in value:
        pairs.append(
            (
                f"{prefix}.PermissionsBoundaryUsageCount",
                str(value["permissions_boundary_usage_count"]),
            )
        )
    pairs.append(
        (
            f"{prefix}.IsAttachable",
            "true" if value.get("is_attachable", False) else "false",
        )
    )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "create_date" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "update_date" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["update_date"], pairs, f"{prefix}.UpdateDate"
        )
    if "tags" in value:
        import aws_sdk_iam.types.tag_list_type

        aws_sdk_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> Policy:
    out: Policy = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_policy_id = el.find("PolicyId")
    if child_policy_id is not None:
        out["policy_id"] = str(child_policy_id.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_default_version_id = el.find("DefaultVersionId")
    if child_default_version_id is not None:
        out["default_version_id"] = str(child_default_version_id.text or "")
    child_attachment_count = el.find("AttachmentCount")
    if child_attachment_count is not None:
        out["attachment_count"] = int(child_attachment_count.text or "")
    child_permissions_boundary_usage_count = el.find("PermissionsBoundaryUsageCount")
    if child_permissions_boundary_usage_count is not None:
        out["permissions_boundary_usage_count"] = int(
            child_permissions_boundary_usage_count.text or ""
        )
    child_is_attachable = el.find("IsAttachable")
    if child_is_attachable is not None:
        out["is_attachable"] = (child_is_attachable.text or "").lower() == "true"
    else:
        out["is_attachable"] = False
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_iam.types.date_type

        out["create_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_create_date
        )
    child_update_date = el.find("UpdateDate")
    if child_update_date is not None:
        import aws_sdk_iam.types.date_type

        out["update_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_update_date
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
