"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

IntegrationStatus: TypeAlias = Literal[
    "PROVISIONING",
    "ACTIVE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IntegrationStatus:
    return cast(IntegrationStatus, data)
