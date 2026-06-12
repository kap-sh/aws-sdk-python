"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_summary

ApplicationSummaries: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.application_summary.ApplicationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSummaries) -> list:
    import aws_sdk_kinesis_analytics_v2.types.application_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.application_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationSummaries:
    import aws_sdk_kinesis_analytics_v2.types.application_summary

    out: ApplicationSummaries = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.application_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
