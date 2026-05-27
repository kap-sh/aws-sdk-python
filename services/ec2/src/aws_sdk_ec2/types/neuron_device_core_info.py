"""Generated from Smithy shape ``com.amazonaws.ec2#NeuronDeviceCoreInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.neuron_device_core_count
    import aws_sdk_ec2.types.neuron_device_core_version


class NeuronDeviceCoreInfo(TypedDict):
    count: NotRequired[
        "aws_sdk_ec2.types.neuron_device_core_count.NeuronDeviceCoreCount"
    ]
    """<p>The number of cores available to the neuron accelerator.</p>"""
    version: NotRequired[
        "aws_sdk_ec2.types.neuron_device_core_version.NeuronDeviceCoreVersion"
    ]
    """<p>The version of the neuron accelerator.</p>"""
