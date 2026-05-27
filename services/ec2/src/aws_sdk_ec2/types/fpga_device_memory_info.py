"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaDeviceMemoryInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_device_memory_size


class FpgaDeviceMemoryInfo(TypedDict):
    size_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.fpga_device_memory_size.FpgaDeviceMemorySize"
    ]
    """<p>The size of the memory available to the FPGA accelerator, in MiB.</p>"""
