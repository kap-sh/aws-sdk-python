"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#InstanceBlockDeviceMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snow_device_management.types.ebs_instance_block_device


class InstanceBlockDeviceMapping(TypedDict, closed=True):
    device_name: NotRequired["str"]
    """<p>The block device name.</p>"""
    ebs: NotRequired[
        "capo_snow_device_management.types.ebs_instance_block_device.EbsInstanceBlockDevice"
    ]
    """<p>The parameters used to automatically set up Amazon Elastic Block Store (Amazon EBS) volumes when the instance is launched. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceBlockDeviceMapping) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    if "ebs" in value:
        import capo_snow_device_management.types.ebs_instance_block_device

        out["ebs"] = (
            capo_snow_device_management.types.ebs_instance_block_device.serialize_json(
                value["ebs"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceBlockDeviceMapping:
    out: InstanceBlockDeviceMapping = {}  # type: ignore[typeddict-item]
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    if "ebs" in data:
        import capo_snow_device_management.types.ebs_instance_block_device

        out["ebs"] = (
            capo_snow_device_management.types.ebs_instance_block_device.deserialize_json(
                data["ebs"]
            )
        )
    return out
