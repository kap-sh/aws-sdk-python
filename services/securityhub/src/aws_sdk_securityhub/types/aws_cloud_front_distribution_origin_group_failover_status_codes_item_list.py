"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginGroupFailoverStatusCodesItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer

AwsCloudFrontDistributionOriginGroupFailoverStatusCodesItemList: TypeAlias = list[
    "aws_sdk_securityhub.types.integer.Integer"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsCloudFrontDistributionOriginGroupFailoverStatusCodesItemList,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> AwsCloudFrontDistributionOriginGroupFailoverStatusCodesItemList:
    return list(data)
