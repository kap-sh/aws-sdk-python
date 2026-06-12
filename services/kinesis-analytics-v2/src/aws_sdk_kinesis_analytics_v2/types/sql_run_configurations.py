"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SqlRunConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.sql_run_configuration

SqlRunConfigurations: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.sql_run_configuration.SqlRunConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlRunConfigurations) -> list:
    import aws_sdk_kinesis_analytics_v2.types.sql_run_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.sql_run_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SqlRunConfigurations:
    import aws_sdk_kinesis_analytics_v2.types.sql_run_configuration

    out: SqlRunConfigurations = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.sql_run_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
