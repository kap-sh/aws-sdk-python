"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsAction``."""

from typing import Literal, TypeAlias, cast

ContributorInsightsAction: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContributorInsightsAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContributorInsightsAction:
    return cast(ContributorInsightsAction, data)
