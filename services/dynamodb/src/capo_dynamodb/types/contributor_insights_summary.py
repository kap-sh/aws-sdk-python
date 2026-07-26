"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.contributor_insights_mode
    import capo_dynamodb.types.contributor_insights_status
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.table_name


class ContributorInsightsSummary(TypedDict, closed=True):
    table_name: NotRequired["capo_dynamodb.types.table_name.TableName"]
    """<p>Name of the table associated with the summary.</p>"""
    index_name: NotRequired["capo_dynamodb.types.index_name.IndexName"]
    """<p>Name of the index associated with the summary, if any.</p>"""
    contributor_insights_status: NotRequired[
        "capo_dynamodb.types.contributor_insights_status.ContributorInsightsStatus"
    ]
    """<p>Describes the current status for contributor insights for the given table and index, if applicable.</p>"""
    contributor_insights_mode: NotRequired[
        "capo_dynamodb.types.contributor_insights_mode.ContributorInsightsMode"
    ]
    """<p>Indicates the current mode of CloudWatch Contributor Insights, specifying whether it tracks all access and throttled events or throttled events only for the DynamoDB table or index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContributorInsightsSummary) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "contributor_insights_status" in value:
        import capo_dynamodb.types.contributor_insights_status

        out["ContributorInsightsStatus"] = (
            capo_dynamodb.types.contributor_insights_status.serialize_aws_json_1_0(
                value["contributor_insights_status"]
            )
        )
    if "contributor_insights_mode" in value:
        import capo_dynamodb.types.contributor_insights_mode

        out["ContributorInsightsMode"] = (
            capo_dynamodb.types.contributor_insights_mode.serialize_aws_json_1_0(
                value["contributor_insights_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ContributorInsightsSummary:
    out: ContributorInsightsSummary = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "ContributorInsightsStatus" in data:
        import capo_dynamodb.types.contributor_insights_status

        out["contributor_insights_status"] = (
            capo_dynamodb.types.contributor_insights_status.deserialize_aws_json_1_0(
                data["ContributorInsightsStatus"]
            )
        )
    if "ContributorInsightsMode" in data:
        import capo_dynamodb.types.contributor_insights_mode

        out["contributor_insights_mode"] = (
            capo_dynamodb.types.contributor_insights_mode.deserialize_aws_json_1_0(
                data["ContributorInsightsMode"]
            )
        )
    return out
