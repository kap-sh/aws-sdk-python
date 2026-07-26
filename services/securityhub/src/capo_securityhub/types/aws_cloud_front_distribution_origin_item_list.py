"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_item

AwsCloudFrontDistributionOriginItemList: TypeAlias = list[
    "capo_securityhub.types.aws_cloud_front_distribution_origin_item.AwsCloudFrontDistributionOriginItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginItemList) -> list:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_item

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_cloud_front_distribution_origin_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsCloudFrontDistributionOriginItemList:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_item

    out: AwsCloudFrontDistributionOriginItemList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_cloud_front_distribution_origin_item.deserialize_json(
                item
            )
        )
    return out
