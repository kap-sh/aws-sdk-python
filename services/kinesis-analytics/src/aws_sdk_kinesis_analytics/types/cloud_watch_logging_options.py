"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CloudWatchLoggingOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option

CloudWatchLoggingOptions: TypeAlias = list[
    "aws_sdk_kinesis_analytics.types.cloud_watch_logging_option.CloudWatchLoggingOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOptions) -> list:
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_option.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CloudWatchLoggingOptions:
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option

    out: CloudWatchLoggingOptions = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_option.deserialize_aws_json_1_1(
                item
            )
        )
    return out
