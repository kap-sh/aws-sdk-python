"""Generated from Smithy shape ``com.amazonaws.ec2#MediaAcceleratorInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.media_device_info_list
    import aws_sdk_ec2.types.total_media_memory


class MediaAcceleratorInfo(TypedDict):
    accelerators: NotRequired[
        "aws_sdk_ec2.types.media_device_info_list.MediaDeviceInfoList"
    ]
    """<p>Describes the media accelerators for the instance type.</p>"""
    total_media_memory_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.total_media_memory.TotalMediaMemory"
    ]
    """<p>The total size of the memory for the media accelerators for the instance type, in MiB.</p>"""
