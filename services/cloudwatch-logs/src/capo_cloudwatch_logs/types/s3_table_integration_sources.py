"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#S3TableIntegrationSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.s3_table_integration_source

S3TableIntegrationSources: TypeAlias = list[
    "capo_cloudwatch_logs.types.s3_table_integration_source.S3TableIntegrationSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TableIntegrationSources) -> list:
    import capo_cloudwatch_logs.types.s3_table_integration_source

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.s3_table_integration_source.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> S3TableIntegrationSources:
    import capo_cloudwatch_logs.types.s3_table_integration_source

    out: S3TableIntegrationSources = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.s3_table_integration_source.deserialize_aws_json_1_1(
                item
            )
        )
    return out
