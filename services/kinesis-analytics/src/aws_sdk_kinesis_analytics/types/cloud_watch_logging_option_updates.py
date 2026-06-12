"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CloudWatchLoggingOptionUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_update

CloudWatchLoggingOptionUpdates: TypeAlias = list[
    "aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_update.CloudWatchLoggingOptionUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOptionUpdates) -> list:
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CloudWatchLoggingOptionUpdates:
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_update

    out: CloudWatchLoggingOptionUpdates = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out
