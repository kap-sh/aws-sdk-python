"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterfaceAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attachment_status
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class SecondaryInterfaceAttachment(TypedDict, closed=True):
    attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the attachment.</p>"""
    attach_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The timestamp when the attachment was created.</p>"""
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the secondary interface is deleted when the instance is terminated.</p> <p>The only supported value for this field is <code>true</code>.</p>"""
    device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The device index of the secondary interface.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance to which the secondary interface is attached.</p>"""
    instance_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the instance.</p>"""
    network_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the network card.</p>"""
    status: NotRequired["capo_ec2.types.attachment_status.AttachmentStatus"]
    """<p>The attachment state.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecondaryInterfaceAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attachment_id" in value:
        pairs.append((f"{key_prefix}AttachmentId", str(value["attachment_id"])))
    if "attach_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["attach_time"], pairs, f"{key_prefix}AttachTime"
        )
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "device_index" in value:
        pairs.append((f"{key_prefix}DeviceIndex", str(value["device_index"])))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "instance_owner_id" in value:
        pairs.append((f"{key_prefix}InstanceOwnerId", str(value["instance_owner_id"])))
    if "network_card_index" in value:
        pairs.append(
            (f"{key_prefix}NetworkCardIndex", str(value["network_card_index"]))
        )
    if "status" in value:
        import capo_ec2.types.attachment_status

        capo_ec2.types.attachment_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_ec2_query(el: Element) -> SecondaryInterfaceAttachment:
    out: SecondaryInterfaceAttachment = {}  # type: ignore[typeddict-item]
    child_attachment_id = el.find("AttachmentId")
    if child_attachment_id is not None:
        out["attachment_id"] = str(child_attachment_id.text or "")
    child_attach_time = el.find("AttachTime")
    if child_attach_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["attach_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_attach_time
        )
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_device_index = el.find("DeviceIndex")
    if child_device_index is not None:
        out["device_index"] = int(child_device_index.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_owner_id = el.find("InstanceOwnerId")
    if child_instance_owner_id is not None:
        out["instance_owner_id"] = str(child_instance_owner_id.text or "")
    child_network_card_index = el.find("NetworkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.attachment_status

        out["status"] = capo_ec2.types.attachment_status.deserialize_ec2_query(
            child_status
        )
    return out
