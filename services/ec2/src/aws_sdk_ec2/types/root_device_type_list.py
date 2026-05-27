"""Generated from Smithy shape ``com.amazonaws.ec2#RootDeviceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.root_device_type

RootDeviceTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.root_device_type.RootDeviceType"
]
