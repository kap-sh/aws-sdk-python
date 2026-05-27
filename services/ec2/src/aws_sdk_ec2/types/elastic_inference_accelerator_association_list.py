"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticInferenceAcceleratorAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_inference_accelerator_association

ElasticInferenceAcceleratorAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.elastic_inference_accelerator_association.ElasticInferenceAcceleratorAssociation"
]
