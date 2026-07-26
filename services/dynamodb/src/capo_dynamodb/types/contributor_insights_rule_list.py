"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.contributor_insights_rule

ContributorInsightsRuleList: TypeAlias = list[
    "capo_dynamodb.types.contributor_insights_rule.ContributorInsightsRule"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContributorInsightsRuleList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ContributorInsightsRuleList:
    return list(data)
