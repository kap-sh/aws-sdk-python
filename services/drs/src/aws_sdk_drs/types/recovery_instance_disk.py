"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDisk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.bounded_string
    import aws_sdk_drs.types.ebs_volume_id
    import aws_sdk_drs.types.positive_integer


class RecoveryInstanceDisk(TypedDict, closed=True):
    internal_device_name: NotRequired["aws_sdk_drs.types.bounded_string.BoundedString"]
    """<p>The internal device name of this disk. This is the name that is visible on the machine itself and not from the EC2 console.</p>"""
    bytes: "aws_sdk_drs.types.positive_integer.PositiveInteger"
    """<p>The amount of storage on the disk in bytes.</p>"""
    ebs_volume_id: NotRequired["aws_sdk_drs.types.ebs_volume_id.EbsVolumeID"]
    """<p>The EBS Volume ID of this disk.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDisk) -> dict:
    out: dict = {}
    if "internal_device_name" in value:
        out["internalDeviceName"] = value["internal_device_name"]
    out["bytes"] = value.get("bytes", 0)
    if "ebs_volume_id" in value:
        out["ebsVolumeID"] = value["ebs_volume_id"]
    return out


def deserialize_json(data: dict) -> RecoveryInstanceDisk:
    out: RecoveryInstanceDisk = {}  # type: ignore[typeddict-item]
    if "internalDeviceName" in data:
        out["internal_device_name"] = data["internalDeviceName"]
    if "bytes" in data:
        out["bytes"] = data["bytes"]
    else:
        out["bytes"] = 0
    if "ebsVolumeID" in data:
        out["ebs_volume_id"] = data["ebsVolumeID"]
    return out
