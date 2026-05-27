"""Generated from Smithy shape ``com.amazonaws.ecs#InferenceAcceleratorOverride``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class InferenceAcceleratorOverride(TypedDict):
    device_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Elastic Inference accelerator device name to override for the task. This parameter must match a <code>deviceName</code> specified in the task definition.</p>"""
    device_type: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Elastic Inference accelerator type to use.</p>"""
