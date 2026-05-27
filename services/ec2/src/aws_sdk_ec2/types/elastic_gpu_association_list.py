"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_association

ElasticGpuAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.elastic_gpu_association.ElasticGpuAssociation"
]
