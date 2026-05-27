"""Generated from Smithy shape ``com.amazonaws.ec2#InferenceDeviceMemoryInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.inference_device_memory_size


class InferenceDeviceMemoryInfo(TypedDict):
    size_in_mi_b: NotRequired[
        "aws_sdk_ec2.types.inference_device_memory_size.InferenceDeviceMemorySize"
    ]
    """<p>The size of the memory available to the inference accelerator, in MiB.</p>"""
