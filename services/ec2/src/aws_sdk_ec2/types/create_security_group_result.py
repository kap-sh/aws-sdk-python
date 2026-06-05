"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSecurityGroupResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CreateSecurityGroupResult(TypedDict):
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the security group.</p>"""
    security_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group ARN.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSecurityGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "security_group_arn" in value:
        pairs.append((f"{prefix}.SecurityGroupArn", str(value["security_group_arn"])))


def deserialize_ec2_query(el: Element) -> CreateSecurityGroupResult:
    out: CreateSecurityGroupResult = {}  # type: ignore[typeddict-item]
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_security_group_arn = el.find("SecurityGroupArn")
    if child_security_group_arn is not None:
        out["security_group_arn"] = str(child_security_group_arn.text or "")
    return out
