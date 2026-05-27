"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.contributor_insights_rule

ContributorInsightsRuleList: TypeAlias = list[
    "aws_sdk_dynamodb.types.contributor_insights_rule.ContributorInsightsRule"
]
