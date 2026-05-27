"""Generated from Smithy shape ``com.amazonaws.ec2#InferenceAcceleratorInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.inference_device_info_list
    import aws_sdk_ec2.types.total_inference_memory


class InferenceAcceleratorInfo(TypedDict):
    accelerators: NotRequired[
        "aws_sdk_ec2.types.inference_device_info_list.InferenceDeviceInfoList"
    ]
    """<p>Describes the Inference accelerators for the instance type.</p>"""
    total_inference_memory_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.total_inference_memory.totalInferenceMemory"
    ]
    """<p>The total size of the memory for the inference accelerators for the instance type, in MiB.</p>"""
