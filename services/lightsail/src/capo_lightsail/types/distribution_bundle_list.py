"""Generated from Smithy shape ``com.amazonaws.lightsail#DistributionBundleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.distribution_bundle

DistributionBundleList: TypeAlias = list[
    "capo_lightsail.types.distribution_bundle.DistributionBundle"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributionBundleList) -> list:
    import capo_lightsail.types.distribution_bundle

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.distribution_bundle.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DistributionBundleList:
    import capo_lightsail.types.distribution_bundle

    out: DistributionBundleList = []
    for item in data:
        out.append(
            capo_lightsail.types.distribution_bundle.deserialize_aws_json_1_1(item)
        )
    return out
