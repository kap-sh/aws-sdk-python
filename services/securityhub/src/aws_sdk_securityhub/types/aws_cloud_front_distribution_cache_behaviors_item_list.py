"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionCacheBehaviorsItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behavior

AwsCloudFrontDistributionCacheBehaviorsItemList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behavior.AwsCloudFrontDistributionCacheBehavior"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionCacheBehaviorsItemList) -> list:
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behavior

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behavior.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsCloudFrontDistributionCacheBehaviorsItemList:
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behavior

    out: AwsCloudFrontDistributionCacheBehaviorsItemList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behavior.deserialize_json(
                item
            )
        )
    return out
