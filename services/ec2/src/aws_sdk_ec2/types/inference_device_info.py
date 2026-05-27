"""Generated from Smithy shape ``com.amazonaws.ec2#InferenceDeviceInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.inference_device_count
    import aws_sdk_ec2.types.inference_device_manufacturer_name
    import aws_sdk_ec2.types.inference_device_memory_info
    import aws_sdk_ec2.types.inference_device_name


class InferenceDeviceInfo(TypedDict):
    count: NotRequired["aws_sdk_ec2.types.inference_device_count.InferenceDeviceCount"]
    """<p>The number of Inference accelerators for the instance type.</p>"""
    name: NotRequired["aws_sdk_ec2.types.inference_device_name.InferenceDeviceName"]
    """<p>The name of the Inference accelerator.</p>"""
    manufacturer: NotRequired[
        "aws_sdk_ec2.types.inference_device_manufacturer_name.InferenceDeviceManufacturerName"
    ]
    """<p>The manufacturer of the Inference accelerator.</p>"""
    memory_info: NotRequired[
        "aws_sdk_ec2.types.inference_device_memory_info.InferenceDeviceMemoryInfo"
    ]
    """<p>Describes the memory available to the inference accelerator.</p>"""
