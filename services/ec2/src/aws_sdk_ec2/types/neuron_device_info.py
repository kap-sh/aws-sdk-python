"""Generated from Smithy shape ``com.amazonaws.ec2#NeuronDeviceInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.neuron_device_core_info
    import aws_sdk_ec2.types.neuron_device_count
    import aws_sdk_ec2.types.neuron_device_memory_info
    import aws_sdk_ec2.types.neuron_device_name


class NeuronDeviceInfo(TypedDict):
    count: NotRequired["aws_sdk_ec2.types.neuron_device_count.NeuronDeviceCount"]
    """<p>The number of neuron accelerators for the instance type.</p>"""
    name: NotRequired["aws_sdk_ec2.types.neuron_device_name.NeuronDeviceName"]
    """<p>The name of the neuron accelerator.</p>"""
    core_info: NotRequired[
        "aws_sdk_ec2.types.neuron_device_core_info.NeuronDeviceCoreInfo"
    ]
    """<p>Describes the cores available to each neuron accelerator.</p>"""
    memory_info: NotRequired[
        "aws_sdk_ec2.types.neuron_device_memory_info.NeuronDeviceMemoryInfo"
    ]
    """<p>Describes the memory available to each neuron accelerator.</p>"""
