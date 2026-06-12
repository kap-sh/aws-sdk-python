"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginGroupsItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group

AwsCloudFrontDistributionOriginGroupsItemList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group.AwsCloudFrontDistributionOriginGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginGroupsItemList) -> list:
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsCloudFrontDistributionOriginGroupsItemList:
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group

    out: AwsCloudFrontDistributionOriginGroupsItemList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group.deserialize_json(
                item
            )
        )
    return out
