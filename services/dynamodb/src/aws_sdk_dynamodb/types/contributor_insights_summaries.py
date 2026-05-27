"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.contributor_insights_summary

ContributorInsightsSummaries: TypeAlias = list[
    "aws_sdk_dynamodb.types.contributor_insights_summary.ContributorInsightsSummary"
]
