"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateElasticInferenceAcceleratorResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_response

LaunchTemplateElasticInferenceAcceleratorResponseList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_response.LaunchTemplateElasticInferenceAcceleratorResponse"
]
