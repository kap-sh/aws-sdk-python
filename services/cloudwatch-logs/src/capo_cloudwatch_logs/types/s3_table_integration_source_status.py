"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#S3TableIntegrationSourceStatus``."""

from typing import Literal, TypeAlias, cast

S3TableIntegrationSourceStatus: TypeAlias = Literal[
    "ACTIVE",
    "UNHEALTHY",
    "FAILED",
    "DATA_SOURCE_DELETE_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TableIntegrationSourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3TableIntegrationSourceStatus:
    return cast(S3TableIntegrationSourceStatus, data)
