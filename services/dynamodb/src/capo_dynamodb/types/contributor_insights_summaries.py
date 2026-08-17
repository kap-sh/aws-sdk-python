"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.contributor_insights_summary

ContributorInsightsSummaries: TypeAlias = list[
    "capo_dynamodb.types.contributor_insights_summary.ContributorInsightsSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContributorInsightsSummaries) -> list:
    import capo_dynamodb.types.contributor_insights_summary

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.contributor_insights_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ContributorInsightsSummaries:
    import capo_dynamodb.types.contributor_insights_summary

    out: ContributorInsightsSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.contributor_insights_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
