"""Generated from Smithy shape ``com.amazonaws.ec2#NeuronDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.neuron_device_info

NeuronDeviceInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.neuron_device_info.NeuronDeviceInfo"
]
