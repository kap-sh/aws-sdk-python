"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusAttachmentStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class VolumeStatusAttachmentStatus(TypedDict, closed=True):
    io_performance: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum IOPS supported by the attached instance.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the attached instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeStatusAttachmentStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "io_performance" in value:
        pairs.append((f"{prefix}.IoPerformance", str(value["io_performance"])))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))


def deserialize_ec2_query(el: Element) -> VolumeStatusAttachmentStatus:
    out: VolumeStatusAttachmentStatus = {}  # type: ignore[typeddict-item]
    child_io_performance = el.find("IoPerformance")
    if child_io_performance is not None:
        out["io_performance"] = str(child_io_performance.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    return out
