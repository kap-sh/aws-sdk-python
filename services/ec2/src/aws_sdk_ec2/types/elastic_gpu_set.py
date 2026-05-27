"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpus

ElasticGpuSet: TypeAlias = list["aws_sdk_ec2.types.elastic_gpus.ElasticGpus"]
