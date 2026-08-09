"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowAssociationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dedicated_host_id_list
    import capo_ec2.types.instance_id_list
    import capo_ec2.types.tag_list


class InstanceEventWindowAssociationTarget(TypedDict, closed=True):
    instance_ids: NotRequired["capo_ec2.types.instance_id_list.InstanceIdList"]
    """<p>The IDs of the instances associated with the event window.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The instance tags associated with the event window. Any instances associated with the tags will be associated with the event window.</p> <p>Note that while you can't create tag keys beginning with <code>aws:</code>, you can specify existing Amazon Web Services managed tag keys (with the <code>aws:</code> prefix) when specifying them as targets to associate with the event window.</p>"""
    dedicated_host_ids: NotRequired[
        "capo_ec2.types.dedicated_host_id_list.DedicatedHostIdList"
    ]
    """<p>The IDs of the Dedicated Hosts associated with the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindowAssociationTarget,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_list

        capo_ec2.types.instance_id_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceIdSet"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "dedicated_host_ids" in value:
        import capo_ec2.types.dedicated_host_id_list

        capo_ec2.types.dedicated_host_id_list.serialize_ec2_query(
            value["dedicated_host_ids"], pairs, f"{key_prefix}DedicatedHostIdSet"
        )


def deserialize_ec2_query(el: Element) -> InstanceEventWindowAssociationTarget:
    out: InstanceEventWindowAssociationTarget = {}  # type: ignore[typeddict-item]
    child_instance_ids = el.find("instanceIdSet")
    if child_instance_ids is not None:
        import capo_ec2.types.instance_id_list

        out["instance_ids"] = capo_ec2.types.instance_id_list.deserialize_ec2_query(
            child_instance_ids
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_dedicated_host_ids = el.find("dedicatedHostIdSet")
    if child_dedicated_host_ids is not None:
        import capo_ec2.types.dedicated_host_id_list

        out["dedicated_host_ids"] = (
            capo_ec2.types.dedicated_host_id_list.deserialize_ec2_query(
                child_dedicated_host_ids
            )
        )
    return out
