"""Generated from Smithy shape ``com.amazonaws.ecs#EBSTagSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.ebs_tag_specification

EBSTagSpecifications: TypeAlias = list[
    "aws_sdk_ecs.types.ebs_tag_specification.EBSTagSpecification"
]
