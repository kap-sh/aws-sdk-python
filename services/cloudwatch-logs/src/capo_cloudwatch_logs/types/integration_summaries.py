"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IntegrationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.integration_summary

IntegrationSummaries: TypeAlias = list[
    "capo_cloudwatch_logs.types.integration_summary.IntegrationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationSummaries) -> list:
    import capo_cloudwatch_logs.types.integration_summary

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.integration_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IntegrationSummaries:
    import capo_cloudwatch_logs.types.integration_summary

    out: IntegrationSummaries = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.integration_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
