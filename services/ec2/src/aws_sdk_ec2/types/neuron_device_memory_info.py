"""Generated from Smithy shape ``com.amazonaws.ec2#NeuronDeviceMemoryInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.neuron_device_memory_size


class NeuronDeviceMemoryInfo(TypedDict):
    size_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.neuron_device_memory_size.NeuronDeviceMemorySize"
    ]
    """<p>The size of the memory available to the neuron accelerator, in MiB.</p>"""
