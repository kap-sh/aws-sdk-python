"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CloudWatchLoggingOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_option

CloudWatchLoggingOptions: TypeAlias = list[
    "capo_kinesis_analytics_v2.types.cloud_watch_logging_option.CloudWatchLoggingOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOptions) -> list:
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_option

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics_v2.types.cloud_watch_logging_option.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CloudWatchLoggingOptions:
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_option

    out: CloudWatchLoggingOptions = []
    for item in data:
        out.append(
            capo_kinesis_analytics_v2.types.cloud_watch_logging_option.deserialize_aws_json_1_1(
                item
            )
        )
    return out
