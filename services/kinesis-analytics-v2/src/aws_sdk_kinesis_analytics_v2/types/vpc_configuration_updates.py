"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#VpcConfigurationUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.vpc_configuration_update

VpcConfigurationUpdates: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.vpc_configuration_update.VpcConfigurationUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfigurationUpdates) -> list:
    import aws_sdk_kinesis_analytics_v2.types.vpc_configuration_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.vpc_configuration_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VpcConfigurationUpdates:
    import aws_sdk_kinesis_analytics_v2.types.vpc_configuration_update

    out: VpcConfigurationUpdates = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.vpc_configuration_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out
