"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dedicated_host_id_list
    import capo_ec2.types.instance_id_list
    import capo_ec2.types.tag_list


class InstanceEventWindowAssociationRequest(TypedDict, closed=True):
    instance_ids: NotRequired["capo_ec2.types.instance_id_list.InstanceIdList"]
    """<p>The IDs of the instances to associate with the event window. If the instance is on a Dedicated Host, you can't specify the Instance ID parameter; you must use the Dedicated Host ID parameter.</p>"""
    instance_tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The instance tags to associate with the event window. Any instances associated with the tags will be associated with the event window.</p> <p>Note that while you can't create tag keys beginning with <code>aws:</code>, you can specify existing Amazon Web Services managed tag keys (with the <code>aws:</code> prefix) when specifying them as targets to associate with the event window.</p>"""
    dedicated_host_ids: NotRequired[
        "capo_ec2.types.dedicated_host_id_list.DedicatedHostIdList"
    ]
    """<p>The IDs of the Dedicated Hosts to associate with the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindowAssociationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_list

        capo_ec2.types.instance_id_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceIds"
        )
    if "instance_tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["instance_tags"], pairs, f"{key_prefix}InstanceTags"
        )
    if "dedicated_host_ids" in value:
        import capo_ec2.types.dedicated_host_id_list

        capo_ec2.types.dedicated_host_id_list.serialize_ec2_query(
            value["dedicated_host_ids"], pairs, f"{key_prefix}DedicatedHostIds"
        )


def deserialize_ec2_query(el: Element) -> InstanceEventWindowAssociationRequest:
    out: InstanceEventWindowAssociationRequest = {}  # type: ignore[typeddict-item]
    if el.find("InstanceIds") is not None:
        import capo_ec2.types.instance_id_list

        out["instance_ids"] = capo_ec2.types.instance_id_list.deserialize_ec2_query(
            el, "InstanceIds"
        )
    if el.find("InstanceTags") is not None:
        import capo_ec2.types.tag_list

        out["instance_tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(
            el, "InstanceTags"
        )
    if el.find("DedicatedHostIds") is not None:
        import capo_ec2.types.dedicated_host_id_list

        out["dedicated_host_ids"] = (
            capo_ec2.types.dedicated_host_id_list.deserialize_ec2_query(
                el, "DedicatedHostIds"
            )
        )
    return out
