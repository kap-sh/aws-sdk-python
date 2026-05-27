"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListContributorInsightsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.contributor_insights_summaries
    import aws_sdk_dynamodb.types.next_token_string


class ListContributorInsightsOutput(TypedDict):
    contributor_insights_summaries: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_summaries.ContributorInsightsSummaries"
    ]
    """<p>A list of ContributorInsightsSummary.</p>"""
    next_token: NotRequired["aws_sdk_dynamodb.types.next_token_string.NextTokenString"]
    """<p>A token to go to the next page if there is one.</p>"""
