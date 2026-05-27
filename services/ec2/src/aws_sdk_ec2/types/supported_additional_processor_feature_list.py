"""Generated from Smithy shape ``com.amazonaws.ec2#SupportedAdditionalProcessorFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.supported_additional_processor_feature

SupportedAdditionalProcessorFeatureList: TypeAlias = list[
    "aws_sdk_ec2.types.supported_additional_processor_feature.SupportedAdditionalProcessorFeature"
]
