"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attachment_ena_srd_specification
    import aws_sdk_ec2.types.attachment_status
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class NetworkInterfaceAttachment(TypedDict, closed=True):
    attach_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The timestamp indicating when the attachment initiated.</p>"""
    attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface attachment.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is deleted when the instance is terminated.</p>"""
    device_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The device index of the network interface attachment on the instance.</p>"""
    network_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the network card.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the instance.</p>"""
    status: NotRequired["aws_sdk_ec2.types.attachment_status.AttachmentStatus"]
    """<p>The attachment state.</p>"""
    ena_srd_specification: NotRequired[
        "aws_sdk_ec2.types.attachment_ena_srd_specification.AttachmentEnaSrdSpecification"
    ]
    """<p>Configures ENA Express for the network interface that this action attaches to the instance.</p>"""
    ena_queue_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of ENA queues created with the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInterfaceAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attach_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["attach_time"], pairs, f"{prefix}.AttachTime"
        )
    if "attachment_id" in value:
        pairs.append((f"{prefix}.AttachmentId", str(value["attachment_id"])))
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{prefix}.DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "device_index" in value:
        pairs.append((f"{prefix}.DeviceIndex", str(value["device_index"])))
    if "network_card_index" in value:
        pairs.append((f"{prefix}.NetworkCardIndex", str(value["network_card_index"])))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "instance_owner_id" in value:
        pairs.append((f"{prefix}.InstanceOwnerId", str(value["instance_owner_id"])))
    if "status" in value:
        import aws_sdk_ec2.types.attachment_status

        aws_sdk_ec2.types.attachment_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "ena_srd_specification" in value:
        import aws_sdk_ec2.types.attachment_ena_srd_specification

        aws_sdk_ec2.types.attachment_ena_srd_specification.serialize_ec2_query(
            value["ena_srd_specification"], pairs, f"{prefix}.EnaSrdSpecification"
        )
    if "ena_queue_count" in value:
        pairs.append((f"{prefix}.EnaQueueCount", str(value["ena_queue_count"])))


def deserialize_ec2_query(el: Element) -> NetworkInterfaceAttachment:
    out: NetworkInterfaceAttachment = {}  # type: ignore[typeddict-item]
    child_attach_time = el.find("AttachTime")
    if child_attach_time is not None:
        import aws_sdk_ec2.types.date_time

        out["attach_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_attach_time
        )
    child_attachment_id = el.find("AttachmentId")
    if child_attachment_id is not None:
        out["attachment_id"] = str(child_attachment_id.text or "")
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_device_index = el.find("DeviceIndex")
    if child_device_index is not None:
        out["device_index"] = int(child_device_index.text or "")
    child_network_card_index = el.find("NetworkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_owner_id = el.find("InstanceOwnerId")
    if child_instance_owner_id is not None:
        out["instance_owner_id"] = str(child_instance_owner_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.attachment_status

        out["status"] = aws_sdk_ec2.types.attachment_status.deserialize_ec2_query(
            child_status
        )
    child_ena_srd_specification = el.find("EnaSrdSpecification")
    if child_ena_srd_specification is not None:
        import aws_sdk_ec2.types.attachment_ena_srd_specification

        out["ena_srd_specification"] = (
            aws_sdk_ec2.types.attachment_ena_srd_specification.deserialize_ec2_query(
                child_ena_srd_specification
            )
        )
    child_ena_queue_count = el.find("EnaQueueCount")
    if child_ena_queue_count is not None:
        out["ena_queue_count"] = int(child_ena_queue_count.text or "")
    return out
