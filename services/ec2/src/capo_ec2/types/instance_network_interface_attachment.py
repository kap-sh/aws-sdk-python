"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterfaceAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attachment_status
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.instance_attachment_ena_srd_specification
    import capo_ec2.types.integer
    import capo_ec2.types.string


class InstanceNetworkInterfaceAttachment(TypedDict, closed=True):
    attach_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time stamp when the attachment initiated.</p>"""
    attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network interface attachment.</p>"""
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is deleted when the instance is terminated.</p>"""
    device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the device on the instance for the network interface attachment.</p>"""
    status: NotRequired["capo_ec2.types.attachment_status.AttachmentStatus"]
    """<p>The attachment state.</p>"""
    network_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the network card.</p>"""
    ena_srd_specification: NotRequired[
        "capo_ec2.types.instance_attachment_ena_srd_specification.InstanceAttachmentEnaSrdSpecification"
    ]
    """<p>Contains the ENA Express settings for the network interface that's attached to the instance.</p>"""
    ena_queue_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of ENA queues created with the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceNetworkInterfaceAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attach_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["attach_time"], pairs, f"{key_prefix}AttachTime"
        )
    if "attachment_id" in value:
        pairs.append((f"{key_prefix}AttachmentId", str(value["attachment_id"])))
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "device_index" in value:
        pairs.append((f"{key_prefix}DeviceIndex", str(value["device_index"])))
    if "status" in value:
        import capo_ec2.types.attachment_status

        capo_ec2.types.attachment_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "network_card_index" in value:
        pairs.append(
            (f"{key_prefix}NetworkCardIndex", str(value["network_card_index"]))
        )
    if "ena_srd_specification" in value:
        import capo_ec2.types.instance_attachment_ena_srd_specification

        capo_ec2.types.instance_attachment_ena_srd_specification.serialize_ec2_query(
            value["ena_srd_specification"], pairs, f"{key_prefix}EnaSrdSpecification"
        )
    if "ena_queue_count" in value:
        pairs.append((f"{key_prefix}EnaQueueCount", str(value["ena_queue_count"])))


def deserialize_ec2_query(el: Element) -> InstanceNetworkInterfaceAttachment:
    out: InstanceNetworkInterfaceAttachment = {}  # type: ignore[typeddict-item]
    child_attach_time = el.find("attachTime")
    if child_attach_time is not None:
        import capo_ec2.types.date_time

        out["attach_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_attach_time
        )
    child_attachment_id = el.find("attachmentId")
    if child_attachment_id is not None:
        out["attachment_id"] = str(child_attachment_id.text or "")
    child_delete_on_termination = el.find("deleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_device_index = el.find("deviceIndex")
    if child_device_index is not None:
        out["device_index"] = int(child_device_index.text or "")
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.attachment_status

        out["status"] = capo_ec2.types.attachment_status.deserialize_ec2_query(
            child_status
        )
    child_network_card_index = el.find("networkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
    child_ena_srd_specification = el.find("enaSrdSpecification")
    if child_ena_srd_specification is not None:
        import capo_ec2.types.instance_attachment_ena_srd_specification

        out["ena_srd_specification"] = (
            capo_ec2.types.instance_attachment_ena_srd_specification.deserialize_ec2_query(
                child_ena_srd_specification
            )
        )
    child_ena_queue_count = el.find("enaQueueCount")
    if child_ena_queue_count is not None:
        out["ena_queue_count"] = int(child_ena_queue_count.text or "")
    return out
