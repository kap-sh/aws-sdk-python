"""Generated from Smithy shape ``com.amazonaws.redshift#EC2SecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.tag_list


class EC2SecurityGroup(TypedDict, closed=True):
    status: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The status of the EC2 security group.</p>"""
    ec2_security_group_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the EC2 Security Group.</p>"""
    ec2_security_group_owner_id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the EC2 security group specified in the <code>EC2SecurityGroupName</code> field. </p>"""
    tags: NotRequired["aws_sdk_redshift.types.tag_list.TagList"]
    """<p>The list of tags for the EC2 security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EC2SecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "ec2_security_group_name" in value:
        pairs.append(
            (f"{prefix}.EC2SecurityGroupName", str(value["ec2_security_group_name"]))
        )
    if "ec2_security_group_owner_id" in value:
        pairs.append(
            (
                f"{prefix}.EC2SecurityGroupOwnerId",
                str(value["ec2_security_group_owner_id"]),
            )
        )
    if "tags" in value:
        import aws_sdk_redshift.types.tag_list

        aws_sdk_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> EC2SecurityGroup:
    out: EC2SecurityGroup = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_ec2_security_group_name = el.find("EC2SecurityGroupName")
    if child_ec2_security_group_name is not None:
        out["ec2_security_group_name"] = str(child_ec2_security_group_name.text or "")
    child_ec2_security_group_owner_id = el.find("EC2SecurityGroupOwnerId")
    if child_ec2_security_group_owner_id is not None:
        out["ec2_security_group_owner_id"] = str(
            child_ec2_security_group_owner_id.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_redshift.types.tag_list

        out["tags"] = aws_sdk_redshift.types.tag_list.deserialize_query(child_tags)
    return out
