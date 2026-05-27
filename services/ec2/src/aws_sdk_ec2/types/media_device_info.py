"""Generated from Smithy shape ``com.amazonaws.ec2#MediaDeviceInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.media_device_count
    import aws_sdk_ec2.types.media_device_manufacturer_name
    import aws_sdk_ec2.types.media_device_memory_info
    import aws_sdk_ec2.types.media_device_name


class MediaDeviceInfo(TypedDict):
    count: NotRequired["aws_sdk_ec2.types.media_device_count.MediaDeviceCount"]
    """<p>The number of media accelerators for the instance type.</p>"""
    name: NotRequired["aws_sdk_ec2.types.media_device_name.MediaDeviceName"]
    """<p>The name of the media accelerator.</p>"""
    manufacturer: NotRequired[
        "aws_sdk_ec2.types.media_device_manufacturer_name.MediaDeviceManufacturerName"
    ]
    """<p>The manufacturer of the media accelerator.</p>"""
    memory_info: NotRequired[
        "aws_sdk_ec2.types.media_device_memory_info.MediaDeviceMemoryInfo"
    ]
    """<p>Describes the memory available to the media accelerator.</p>"""
