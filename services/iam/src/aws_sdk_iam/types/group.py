"""Generated from Smithy shape ``com.amazonaws.iam#Group``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.group_name_type
    import aws_sdk_iam.types.id_type
    import aws_sdk_iam.types.path_type


class Group(TypedDict):
    path: "aws_sdk_iam.types.path_type.pathType"
    """<p>The path to the group. For more information about paths, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    group_name: "aws_sdk_iam.types.group_name_type.groupNameType"
    """<p>The friendly name that identifies the group.</p>"""
    group_id: "aws_sdk_iam.types.id_type.idType"
    """<p> The stable and unique string identifying the group. For more information about IDs, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    arn: "aws_sdk_iam.types.arn_type.arnType"
    """<p> The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and how to use them in policies, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    create_date: "aws_sdk_iam.types.date_type.dateType"
    """<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the group was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Group, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((f"{prefix}.Path", str(value["path"])))
    pairs.append((f"{prefix}.GroupName", str(value["group_name"])))
    pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    pairs.append((f"{prefix}.Arn", str(value["arn"])))
    import aws_sdk_iam.types.date_type

    aws_sdk_iam.types.date_type.serialize_query(
        value["create_date"], pairs, f"{prefix}.CreateDate"
    )


def deserialize_query(el: Element) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    else:
        raise DeserializationError("Group.path required")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    else:
        raise DeserializationError("Group.group_name required")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    else:
        raise DeserializationError("Group.group_id required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("Group.arn required")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_iam.types.date_type

        out["create_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_create_date
        )
    else:
        raise DeserializationError("Group.create_date required")
    return out
