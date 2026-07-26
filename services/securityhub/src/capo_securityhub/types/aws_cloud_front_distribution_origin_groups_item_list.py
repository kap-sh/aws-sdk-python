"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginGroupsItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_group

AwsCloudFrontDistributionOriginGroupsItemList: TypeAlias = list[
    "capo_securityhub.types.aws_cloud_front_distribution_origin_group.AwsCloudFrontDistributionOriginGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginGroupsItemList) -> list:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_group

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_cloud_front_distribution_origin_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsCloudFrontDistributionOriginGroupsItemList:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_group

    out: AwsCloudFrontDistributionOriginGroupsItemList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_cloud_front_distribution_origin_group.deserialize_json(
                item
            )
        )
    return out
