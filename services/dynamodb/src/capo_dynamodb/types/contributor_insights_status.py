"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsStatus``."""

from typing import Literal, TypeAlias, cast

ContributorInsightsStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContributorInsightsStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContributorInsightsStatus:
    return cast(ContributorInsightsStatus, data)
