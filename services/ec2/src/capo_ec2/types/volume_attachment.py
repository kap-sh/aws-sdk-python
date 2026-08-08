"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.volume_attachment_state


class VolumeAttachment(TypedDict, closed=True):
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the EBS volume is deleted on instance termination.</p>"""
    associated_resource: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the Amazon Web Services-managed resource to which the volume is attached.</p>"""
    instance_owning_service: NotRequired["capo_ec2.types.string.String"]
    """<p>The service principal of the Amazon Web Services service that owns the underlying resource to which the volume is attached.</p> <p>This parameter is returned only for volumes that are attached to Amazon Web Services-managed resources.</p>"""
    ebs_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.</p>"""
    volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the volume.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p> <p>If the volume is attached to an Amazon Web Services-managed resource, this parameter returns <code>null</code>.</p>"""
    device: NotRequired["capo_ec2.types.string.String"]
    """<p>The device name.</p> <p>If the volume is attached to an Amazon Web Services-managed resource, this parameter returns <code>null</code>.</p>"""
    state: NotRequired["capo_ec2.types.volume_attachment_state.VolumeAttachmentState"]
    """<p>The attachment state of the volume.</p>"""
    attach_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time stamp when the attachment initiated.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "associated_resource" in value:
        pairs.append(
            (f"{key_prefix}AssociatedResource", str(value["associated_resource"]))
        )
    if "instance_owning_service" in value:
        pairs.append(
            (
                f"{key_prefix}InstanceOwningService",
                str(value["instance_owning_service"]),
            )
        )
    if "ebs_card_index" in value:
        pairs.append((f"{key_prefix}EbsCardIndex", str(value["ebs_card_index"])))
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "device" in value:
        pairs.append((f"{key_prefix}Device", str(value["device"])))
    if "state" in value:
        import capo_ec2.types.volume_attachment_state

        capo_ec2.types.volume_attachment_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}Status"
        )
    if "attach_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["attach_time"], pairs, f"{key_prefix}AttachTime"
        )


def deserialize_ec2_query(el: Element) -> VolumeAttachment:
    out: VolumeAttachment = {}  # type: ignore[typeddict-item]
    child_delete_on_termination = el.find("deleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_associated_resource = el.find("associatedResource")
    if child_associated_resource is not None:
        out["associated_resource"] = str(child_associated_resource.text or "")
    child_instance_owning_service = el.find("instanceOwningService")
    if child_instance_owning_service is not None:
        out["instance_owning_service"] = str(child_instance_owning_service.text or "")
    child_ebs_card_index = el.find("ebsCardIndex")
    if child_ebs_card_index is not None:
        out["ebs_card_index"] = int(child_ebs_card_index.text or "")
    child_volume_id = el.find("volumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_device = el.find("device")
    if child_device is not None:
        out["device"] = str(child_device.text or "")
    child_state = el.find("status")
    if child_state is not None:
        import capo_ec2.types.volume_attachment_state

        out["state"] = capo_ec2.types.volume_attachment_state.deserialize_ec2_query(
            child_state
        )
    child_attach_time = el.find("attachTime")
    if child_attach_time is not None:
        import capo_ec2.types.date_time

        out["attach_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_attach_time
        )
    return out
