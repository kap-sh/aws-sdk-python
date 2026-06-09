"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfaceAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attachment_status
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class InstanceSecondaryInterfaceAttachment(TypedDict):
    attach_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The timestamp when the attachment was created.</p>"""
    attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the attachment.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the secondary interface is deleted when the instance is terminated.</p> <p>The only supported value for this field is <code>true</code>.</p>"""
    device_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The device index of the secondary interface.</p>"""
    status: NotRequired["aws_sdk_ec2.types.attachment_status.AttachmentStatus"]
    """<p>The attachment state.</p>"""
    network_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the network card.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceSecondaryInterfaceAttachment,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "attach_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
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
    if "status" in value:
        import aws_sdk_ec2.types.attachment_status

        aws_sdk_ec2.types.attachment_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "network_card_index" in value:
        pairs.append((f"{prefix}.NetworkCardIndex", str(value["network_card_index"])))


def deserialize_ec2_query(el: Element) -> InstanceSecondaryInterfaceAttachment:
    out: InstanceSecondaryInterfaceAttachment = {}  # type: ignore[typeddict-item]
    child_attach_time = el.find("AttachTime")
    if child_attach_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["attach_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_attach_time
            )
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
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.attachment_status

        out["status"] = aws_sdk_ec2.types.attachment_status.deserialize_ec2_query(
            child_status
        )
    child_network_card_index = el.find("NetworkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
    return out
