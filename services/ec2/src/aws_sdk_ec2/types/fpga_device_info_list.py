"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_device_info

FpgaDeviceInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.fpga_device_info.FpgaDeviceInfo"
]
