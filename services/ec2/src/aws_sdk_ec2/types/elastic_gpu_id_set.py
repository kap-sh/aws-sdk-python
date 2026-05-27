"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_id

ElasticGpuIdSet: TypeAlias = list["aws_sdk_ec2.types.elastic_gpu_id.ElasticGpuId"]
