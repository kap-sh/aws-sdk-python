"""Generated from Smithy shape ``com.amazonaws.ec2#InferenceDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.inference_device_info

InferenceDeviceInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.inference_device_info.InferenceDeviceInfo"
]
