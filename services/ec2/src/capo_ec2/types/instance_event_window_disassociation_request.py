"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowDisassociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dedicated_host_id_list
    import capo_ec2.types.instance_id_list
    import capo_ec2.types.tag_list


class InstanceEventWindowDisassociationRequest(TypedDict, closed=True):
    instance_ids: NotRequired["capo_ec2.types.instance_id_list.InstanceIdList"]
    """<p>The IDs of the instances to disassociate from the event window.</p>"""
    instance_tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The instance tags to disassociate from the event window. Any instances associated with the tags will be disassociated from the event window.</p>"""
    dedicated_host_ids: NotRequired[
        "capo_ec2.types.dedicated_host_id_list.DedicatedHostIdList"
    ]
    """<p>The IDs of the Dedicated Hosts to disassociate from the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindowDisassociationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_list

        capo_ec2.types.instance_id_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceId"
        )
    if "instance_tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["instance_tags"], pairs, f"{key_prefix}InstanceTag"
        )
    if "dedicated_host_ids" in value:
        import capo_ec2.types.dedicated_host_id_list

        capo_ec2.types.dedicated_host_id_list.serialize_ec2_query(
            value["dedicated_host_ids"], pairs, f"{key_prefix}DedicatedHostId"
        )


def deserialize_ec2_query(el: Element) -> InstanceEventWindowDisassociationRequest:
    out: InstanceEventWindowDisassociationRequest = {}  # type: ignore[typeddict-item]
    child_instance_ids = el.find("InstanceId")
    if child_instance_ids is not None:
        import capo_ec2.types.instance_id_list

        out["instance_ids"] = capo_ec2.types.instance_id_list.deserialize_ec2_query(
            child_instance_ids
        )
    child_instance_tags = el.find("InstanceTag")
    if child_instance_tags is not None:
        import capo_ec2.types.tag_list

        out["instance_tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(
            child_instance_tags
        )
    child_dedicated_host_ids = el.find("DedicatedHostId")
    if child_dedicated_host_ids is not None:
        import capo_ec2.types.dedicated_host_id_list

        out["dedicated_host_ids"] = (
            capo_ec2.types.dedicated_host_id_list.deserialize_ec2_query(
                child_dedicated_host_ids
            )
        )
    return out
