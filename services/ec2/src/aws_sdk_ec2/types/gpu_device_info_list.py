"""Generated from Smithy shape ``com.amazonaws.ec2#GpuDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.gpu_device_info

GpuDeviceInfoList: TypeAlias = list["aws_sdk_ec2.types.gpu_device_info.GpuDeviceInfo"]
