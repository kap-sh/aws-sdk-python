"""Generated from Smithy shape ``com.amazonaws.ec2#ImageNameCriteriaRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_name_criteria_request

ImageNameCriteriaRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.image_name_criteria_request.ImageNameCriteriaRequest"
]
