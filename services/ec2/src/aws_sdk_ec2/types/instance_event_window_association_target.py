"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowAssociationTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dedicated_host_id_list
    import aws_sdk_ec2.types.instance_id_list
    import aws_sdk_ec2.types.tag_list


class InstanceEventWindowAssociationTarget(TypedDict):
    instance_ids: NotRequired["aws_sdk_ec2.types.instance_id_list.InstanceIdList"]
    """<p>The IDs of the instances associated with the event window.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The instance tags associated with the event window. Any instances associated with the tags will be associated with the event window.</p> <p>Note that while you can't create tag keys beginning with <code>aws:</code>, you can specify existing Amazon Web Services managed tag keys (with the <code>aws:</code> prefix) when specifying them as targets to associate with the event window.</p>"""
    dedicated_host_ids: NotRequired[
        "aws_sdk_ec2.types.dedicated_host_id_list.DedicatedHostIdList"
    ]
    """<p>The IDs of the Dedicated Hosts associated with the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindowAssociationTarget,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_ids" in value:
        import aws_sdk_ec2.types.instance_id_list

        aws_sdk_ec2.types.instance_id_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIdSet"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "dedicated_host_ids" in value:
        import aws_sdk_ec2.types.dedicated_host_id_list

        aws_sdk_ec2.types.dedicated_host_id_list.serialize_ec2_query(
            value["dedicated_host_ids"], pairs, f"{prefix}.DedicatedHostIdSet"
        )


def deserialize_ec2_query(el: Element) -> InstanceEventWindowAssociationTarget:
    out: InstanceEventWindowAssociationTarget = {}  # type: ignore[typeddict-item]
    if el.find("InstanceIdSet") is not None:
        import aws_sdk_ec2.types.instance_id_list

        out["instance_ids"] = aws_sdk_ec2.types.instance_id_list.deserialize_ec2_query(
            el, "InstanceIdSet"
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    if el.find("DedicatedHostIdSet") is not None:
        import aws_sdk_ec2.types.dedicated_host_id_list

        out["dedicated_host_ids"] = (
            aws_sdk_ec2.types.dedicated_host_id_list.deserialize_ec2_query(
                el, "DedicatedHostIdSet"
            )
        )
    return out
