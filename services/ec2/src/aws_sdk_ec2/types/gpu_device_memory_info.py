"""Generated from Smithy shape ``com.amazonaws.ec2#GpuDeviceMemoryInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.gpu_device_memory_size


class GpuDeviceMemoryInfo(TypedDict):
    size_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.gpu_device_memory_size.GpuDeviceMemorySize"
    ]
    """<p>The size of the memory available to the GPU accelerator, in MiB.</p>"""
