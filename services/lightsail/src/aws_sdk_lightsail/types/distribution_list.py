"""Generated from Smithy shape ``com.amazonaws.lightsail#DistributionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.lightsail_distribution

DistributionList: TypeAlias = list[
    "aws_sdk_lightsail.types.lightsail_distribution.LightsailDistribution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributionList) -> list:
    import aws_sdk_lightsail.types.lightsail_distribution

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.lightsail_distribution.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DistributionList:
    import aws_sdk_lightsail.types.lightsail_distribution

    out: DistributionList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.lightsail_distribution.deserialize_aws_json_1_1(
                item
            )
        )
    return out
