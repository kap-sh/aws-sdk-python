"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSecurityGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class CreateSecurityGroupResult(TypedDict, closed=True):
    group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the security group.</p>"""
    security_group_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The security group ARN.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSecurityGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "security_group_arn" in value:
        pairs.append(
            (f"{key_prefix}SecurityGroupArn", str(value["security_group_arn"]))
        )


def deserialize_ec2_query(el: Element) -> CreateSecurityGroupResult:
    out: CreateSecurityGroupResult = {}  # type: ignore[typeddict-item]
    child_group_id = el.find("groupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_security_group_arn = el.find("securityGroupArn")
    if child_security_group_arn is not None:
        out["security_group_arn"] = str(child_security_group_arn.text or "")
    return out
