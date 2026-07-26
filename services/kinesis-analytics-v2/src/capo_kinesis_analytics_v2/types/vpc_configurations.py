"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#VpcConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.vpc_configuration

VpcConfigurations: TypeAlias = list[
    "capo_kinesis_analytics_v2.types.vpc_configuration.VpcConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfigurations) -> list:
    import capo_kinesis_analytics_v2.types.vpc_configuration

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics_v2.types.vpc_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VpcConfigurations:
    import capo_kinesis_analytics_v2.types.vpc_configuration

    out: VpcConfigurations = []
    for item in data:
        out.append(
            capo_kinesis_analytics_v2.types.vpc_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
