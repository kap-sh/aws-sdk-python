"""Generated from Smithy shape ``com.amazonaws.ec2#EipAssociationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_ip_association_id

EipAssociationIdList: TypeAlias = list[
    "aws_sdk_ec2.types.elastic_ip_association_id.ElasticIpAssociationId"
]
