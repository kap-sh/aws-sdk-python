"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateElasticInferenceAccelerator``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_count
    import aws_sdk_ec2.types.string


class LaunchTemplateElasticInferenceAccelerator(TypedDict):
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The type of elastic inference accelerator. The possible values are eia1.medium, eia1.large, and eia1.xlarge. </p>"""
    count: NotRequired[
        "aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_count.LaunchTemplateElasticInferenceAcceleratorCount"
    ]
    """<p>The number of elastic inference accelerators to attach to the instance. </p>"""
