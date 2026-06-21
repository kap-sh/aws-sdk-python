"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsMode``."""

from typing import Literal, TypeAlias, cast

ContributorInsightsMode: TypeAlias = Literal[
    "ACCESSED_AND_THROTTLED_KEYS",
    "THROTTLED_KEYS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContributorInsightsMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContributorInsightsMode:
    return cast(ContributorInsightsMode, data)
