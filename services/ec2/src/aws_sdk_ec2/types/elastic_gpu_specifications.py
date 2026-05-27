"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_specification

ElasticGpuSpecifications: TypeAlias = list[
    "aws_sdk_ec2.types.elastic_gpu_specification.ElasticGpuSpecification"
]
