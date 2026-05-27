"""Generated from Smithy shape ``com.amazonaws.ecs#InferenceAccelerator``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class InferenceAccelerator(TypedDict):
    device_name: "aws_sdk_ecs.types.string.String"
    """<p>The Elastic Inference accelerator device name. The <code>deviceName</code> must also be referenced in a container definition as a <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ResourceRequirement.html\">ResourceRequirement</a>.</p>"""
    device_type: "aws_sdk_ecs.types.string.String"
    """<p>The Elastic Inference accelerator type to use.</p>"""
