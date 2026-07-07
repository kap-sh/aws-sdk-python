"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListContributorInsightsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.contributor_insights_summaries
    import aws_sdk_dynamodb.types.next_token_string


class ListContributorInsightsOutput(TypedDict, closed=True):
    contributor_insights_summaries: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_summaries.ContributorInsightsSummaries"
    ]
    """<p>A list of ContributorInsightsSummary.</p>"""
    next_token: NotRequired["aws_sdk_dynamodb.types.next_token_string.NextTokenString"]
    """<p>A token to go to the next page if there is one.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListContributorInsightsOutput) -> dict:
    out: dict = {}
    if "contributor_insights_summaries" in value:
        import aws_sdk_dynamodb.types.contributor_insights_summaries

        out["ContributorInsightsSummaries"] = (
            aws_sdk_dynamodb.types.contributor_insights_summaries.serialize_aws_json_1_0(
                value["contributor_insights_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListContributorInsightsOutput:
    out: ListContributorInsightsOutput = {}  # type: ignore[typeddict-item]
    if "ContributorInsightsSummaries" in data:
        import aws_sdk_dynamodb.types.contributor_insights_summaries

        out["contributor_insights_summaries"] = (
            aws_sdk_dynamodb.types.contributor_insights_summaries.deserialize_aws_json_1_0(
                data["ContributorInsightsSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
