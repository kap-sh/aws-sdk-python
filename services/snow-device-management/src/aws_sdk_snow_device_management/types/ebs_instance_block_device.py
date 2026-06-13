"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#EbsInstanceBlockDevice``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_snow_device_management.types.attachment_status


class EbsInstanceBlockDevice(TypedDict):
    attach_time: NotRequired["datetime.datetime"]
    """<p>When the attachment was initiated.</p>"""
    delete_on_termination: NotRequired["bool"]
    """<p>A value that indicates whether the volume is deleted on instance termination.</p>"""
    status: NotRequired[
        "aws_sdk_snow_device_management.types.attachment_status.AttachmentStatus"
    ]
    """<p>The attachment state.</p>"""
    volume_id: NotRequired["str"]
    """<p>The ID of the Amazon EBS volume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsInstanceBlockDevice) -> dict:
    out: dict = {}
    if "attach_time" in value:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["attachTime"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.serialize_json(
                value["attach_time"]
            )
        )
    if "delete_on_termination" in value:
        out["deleteOnTermination"] = value["delete_on_termination"]
    if "status" in value:
        out["status"] = value["status"]
    if "volume_id" in value:
        out["volumeId"] = value["volume_id"]
    return out


def deserialize_json(data: dict) -> EbsInstanceBlockDevice:
    out: EbsInstanceBlockDevice = {}  # type: ignore[typeddict-item]
    if "attachTime" in data:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["attach_time"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["attachTime"]
            )
        )
    if "deleteOnTermination" in data:
        out["delete_on_termination"] = data["deleteOnTermination"]
    if "status" in data:
        out["status"] = data["status"]
    if "volumeId" in data:
        out["volume_id"] = data["volumeId"]
    return out
