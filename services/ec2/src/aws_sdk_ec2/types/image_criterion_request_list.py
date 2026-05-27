"""Generated from Smithy shape ``com.amazonaws.ec2#ImageCriterionRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_criterion_request

ImageCriterionRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.image_criterion_request.ImageCriterionRequest"
]
