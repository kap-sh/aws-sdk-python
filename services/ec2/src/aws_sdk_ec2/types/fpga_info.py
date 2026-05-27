"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_device_info_list
    import aws_sdk_ec2.types.total_fpga_memory


class FpgaInfo(TypedDict):
    fpgas: NotRequired["aws_sdk_ec2.types.fpga_device_info_list.FpgaDeviceInfoList"]
    """<p>Describes the FPGAs for the instance type.</p>"""
    total_fpga_memory_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.total_fpga_memory.totalFpgaMemory"
    ]
    """<p>The total memory of all FPGA accelerators for the instance type.</p>"""
