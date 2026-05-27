"""Generated from Smithy shape ``com.amazonaws.ec2#GpuInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.gpu_device_info_list
    import aws_sdk_ec2.types.total_gpu_memory


class GpuInfo(TypedDict):
    gpus: NotRequired["aws_sdk_ec2.types.gpu_device_info_list.GpuDeviceInfoList"]
    """<p>Describes the GPU accelerators for the instance type.</p>"""
    total_gpu_memory_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.total_gpu_memory.totalGpuMemory"
    ]
    """<p>The total size of the memory for the GPU accelerators for the instance type, in MiB.</p>"""
