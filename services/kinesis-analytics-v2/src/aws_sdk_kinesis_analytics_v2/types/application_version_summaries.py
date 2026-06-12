"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_version_summary

ApplicationVersionSummaries: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.application_version_summary.ApplicationVersionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationVersionSummaries) -> list:
    import aws_sdk_kinesis_analytics_v2.types.application_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.application_version_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationVersionSummaries:
    import aws_sdk_kinesis_analytics_v2.types.application_version_summary

    out: ApplicationVersionSummaries = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.application_version_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
