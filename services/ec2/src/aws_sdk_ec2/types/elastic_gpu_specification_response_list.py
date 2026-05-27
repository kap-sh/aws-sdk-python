"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuSpecificationResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_specification_response

ElasticGpuSpecificationResponseList: TypeAlias = list[
    "aws_sdk_ec2.types.elastic_gpu_specification_response.ElasticGpuSpecificationResponse"
]
