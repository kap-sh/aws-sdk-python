"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceAttachmentChanges``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.network_interface_attachment_id


class NetworkInterfaceAttachmentChanges(TypedDict, closed=True):
    default_ena_queue_count: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The default number of the ENA queues.</p>"""
    ena_queue_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of ENA queues to be created with the instance.</p>"""
    attachment_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_attachment_id.NetworkInterfaceAttachmentId"
    ]
    """<p>The ID of the network interface attachment.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is deleted when the instance is terminated.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInterfaceAttachmentChanges, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "default_ena_queue_count" in value:
        pairs.append(
            (
                f"{prefix}.DefaultEnaQueueCount",
                "true" if value["default_ena_queue_count"] else "false",
            )
        )
    if "ena_queue_count" in value:
        pairs.append((f"{prefix}.EnaQueueCount", str(value["ena_queue_count"])))
    if "attachment_id" in value:
        pairs.append((f"{prefix}.AttachmentId", str(value["attachment_id"])))
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{prefix}.DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> NetworkInterfaceAttachmentChanges:
    out: NetworkInterfaceAttachmentChanges = {}  # type: ignore[typeddict-item]
    child_default_ena_queue_count = el.find("DefaultEnaQueueCount")
    if child_default_ena_queue_count is not None:
        out["default_ena_queue_count"] = (
            child_default_ena_queue_count.text or ""
        ).lower() == "true"
    child_ena_queue_count = el.find("EnaQueueCount")
    if child_ena_queue_count is not None:
        out["ena_queue_count"] = int(child_ena_queue_count.text or "")
    child_attachment_id = el.find("AttachmentId")
    if child_attachment_id is not None:
        out["attachment_id"] = str(child_attachment_id.text or "")
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    return out
