"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CloudWatchLoggingOptionDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_description

CloudWatchLoggingOptionDescriptions: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_description.CloudWatchLoggingOptionDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOptionDescriptions) -> list:
    import aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CloudWatchLoggingOptionDescriptions:
    import aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_description

    out: CloudWatchLoggingOptionDescriptions = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
