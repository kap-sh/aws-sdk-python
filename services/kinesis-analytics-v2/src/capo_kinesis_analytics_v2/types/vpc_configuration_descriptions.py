"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#VpcConfigurationDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.vpc_configuration_description

VpcConfigurationDescriptions: TypeAlias = list[
    "capo_kinesis_analytics_v2.types.vpc_configuration_description.VpcConfigurationDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfigurationDescriptions) -> list:
    import capo_kinesis_analytics_v2.types.vpc_configuration_description

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics_v2.types.vpc_configuration_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VpcConfigurationDescriptions:
    import capo_kinesis_analytics_v2.types.vpc_configuration_description

    out: VpcConfigurationDescriptions = []
    for item in data:
        out.append(
            capo_kinesis_analytics_v2.types.vpc_configuration_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
