"""Generated from Smithy shape ``com.amazonaws.iam#InstanceProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.id_type
    import aws_sdk_iam.types.instance_profile_name_type
    import aws_sdk_iam.types.path_type
    import aws_sdk_iam.types.role_list_type
    import aws_sdk_iam.types.tag_list_type


class InstanceProfile(TypedDict):
    path: "aws_sdk_iam.types.path_type.pathType"
    r"""<p> The path to the instance profile. For more information about paths, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    instance_profile_name: (
        "aws_sdk_iam.types.instance_profile_name_type.instanceProfileNameType"
    )
    """<p>The name identifying the instance profile.</p>"""
    instance_profile_id: "aws_sdk_iam.types.id_type.idType"
    r"""<p> The stable and unique string identifying the instance profile. For more information about IDs, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    arn: "aws_sdk_iam.types.arn_type.arnType"
    r"""<p> The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    create_date: "aws_sdk_iam.types.date_type.dateType"
    """<p>The date when the instance profile was created.</p>"""
    roles: "aws_sdk_iam.types.role_list_type.roleListType"
    """<p>The role associated with the instance profile.</p>"""
    tags: NotRequired["aws_sdk_iam.types.tag_list_type.tagListType"]
    r"""<p>A list of tags that are attached to the instance profile. For more information about tagging, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html\">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceProfile, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Path", str(value["path"])))
    pairs.append((f"{prefix}.InstanceProfileName", str(value["instance_profile_name"])))
    pairs.append((f"{prefix}.InstanceProfileId", str(value["instance_profile_id"])))
    pairs.append((f"{prefix}.Arn", str(value["arn"])))
    import aws_sdk_iam.types.date_type

    aws_sdk_iam.types.date_type.serialize_query(
        value["create_date"], pairs, f"{prefix}.CreateDate"
    )
    import aws_sdk_iam.types.role_list_type

    aws_sdk_iam.types.role_list_type.serialize_query(
        value["roles"], pairs, f"{prefix}.Roles"
    )
    if "tags" in value:
        import aws_sdk_iam.types.tag_list_type

        aws_sdk_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> InstanceProfile:
    out: InstanceProfile = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    else:
        raise DeserializationError("InstanceProfile.path required")
    child_instance_profile_name = el.find("InstanceProfileName")
    if child_instance_profile_name is not None:
        out["instance_profile_name"] = str(child_instance_profile_name.text or "")
    else:
        raise DeserializationError("InstanceProfile.instance_profile_name required")
    child_instance_profile_id = el.find("InstanceProfileId")
    if child_instance_profile_id is not None:
        out["instance_profile_id"] = str(child_instance_profile_id.text or "")
    else:
        raise DeserializationError("InstanceProfile.instance_profile_id required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("InstanceProfile.arn required")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_iam.types.date_type

        out["create_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_create_date
        )
    else:
        raise DeserializationError("InstanceProfile.create_date required")
    child_roles = el.find("Roles")
    if child_roles is not None:
        import aws_sdk_iam.types.role_list_type

        out["roles"] = aws_sdk_iam.types.role_list_type.deserialize_query(child_roles)
    else:
        raise DeserializationError("InstanceProfile.roles required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
