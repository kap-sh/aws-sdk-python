"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticInferenceAccelerators``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_inference_accelerator

ElasticInferenceAccelerators: TypeAlias = list[
    "aws_sdk_ec2.types.elastic_inference_accelerator.ElasticInferenceAccelerator"
]
