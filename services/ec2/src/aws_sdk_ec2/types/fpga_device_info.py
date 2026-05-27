"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaDeviceInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_device_count
    import aws_sdk_ec2.types.fpga_device_manufacturer_name
    import aws_sdk_ec2.types.fpga_device_memory_info
    import aws_sdk_ec2.types.fpga_device_name


class FpgaDeviceInfo(TypedDict):
    name: NotRequired["aws_sdk_ec2.types.fpga_device_name.FpgaDeviceName"]
    """<p>The name of the FPGA accelerator.</p>"""
    manufacturer: NotRequired[
        "aws_sdk_ec2.types.fpga_device_manufacturer_name.FpgaDeviceManufacturerName"
    ]
    """<p>The manufacturer of the FPGA accelerator.</p>"""
    count: NotRequired["aws_sdk_ec2.types.fpga_device_count.FpgaDeviceCount"]
    """<p>The count of FPGA accelerators for the instance type.</p>"""
    memory_info: NotRequired[
        "aws_sdk_ec2.types.fpga_device_memory_info.FpgaDeviceMemoryInfo"
    ]
    """<p>Describes the memory for the FPGA accelerator for the instance type.</p>"""
