"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLinkInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.group_identifier_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class ClassicLinkInstance(TypedDict, closed=True):
    groups: NotRequired["capo_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>The security groups.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the instance.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClassicLinkInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "groups" in value:
        import capo_ec2.types.group_identifier_list

        capo_ec2.types.group_identifier_list.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}GroupSet"
        )
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> ClassicLinkInstance:
    out: ClassicLinkInstance = {}  # type: ignore[typeddict-item]
    if el.find("GroupSet") is not None:
        import capo_ec2.types.group_identifier_list

        out["groups"] = capo_ec2.types.group_identifier_list.deserialize_ec2_query(
            el, "GroupSet"
        )
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
