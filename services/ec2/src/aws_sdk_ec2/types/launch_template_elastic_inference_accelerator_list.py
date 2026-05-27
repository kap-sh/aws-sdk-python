"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateElasticInferenceAcceleratorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator

LaunchTemplateElasticInferenceAcceleratorList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_elastic_inference_accelerator.LaunchTemplateElasticInferenceAccelerator"
]
