"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupForVpc``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class SecurityGroupForVpc(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The security group's description.</p>"""
    group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The security group name.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The security group owner ID.</p>"""
    group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The security group ID.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The security group tags.</p>"""
    primary_vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The VPC ID in which the security group was created.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupForVpc, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "primary_vpc_id" in value:
        pairs.append((f"{key_prefix}PrimaryVpcId", str(value["primary_vpc_id"])))


def deserialize_ec2_query(el: Element) -> SecurityGroupForVpc:
    out: SecurityGroupForVpc = {}  # type: ignore[typeddict-item]
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_group_name = el.find("groupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_group_id = el.find("groupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_primary_vpc_id = el.find("primaryVpcId")
    if child_primary_vpc_id is not None:
        out["primary_vpc_id"] = str(child_primary_vpc_id.text or "")
    return out
