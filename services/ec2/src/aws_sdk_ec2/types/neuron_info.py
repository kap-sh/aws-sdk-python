"""Generated from Smithy shape ``com.amazonaws.ec2#NeuronInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.neuron_device_info_list
    import aws_sdk_ec2.types.total_neuron_memory


class NeuronInfo(TypedDict):
    neuron_devices: NotRequired[
        "aws_sdk_ec2.types.neuron_device_info_list.NeuronDeviceInfoList"
    ]
    """<p>Describes the neuron accelerators for the instance type.</p>"""
    total_neuron_device_memory_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.total_neuron_memory.TotalNeuronMemory"
    ]
    """<p>The total size of the memory for the neuron accelerators for the instance type, in MiB.</p>"""
