"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateContributorInsightsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.contributor_insights_mode
    import aws_sdk_dynamodb.types.contributor_insights_status
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.table_name


class UpdateContributorInsightsOutput(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>The name of the table.</p>"""
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index, if applicable.</p>"""
    contributor_insights_status: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_status.ContributorInsightsStatus"
    ]
    """<p>The status of contributor insights</p>"""
    contributor_insights_mode: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_mode.ContributorInsightsMode"
    ]
    """<p>The updated mode of CloudWatch Contributor Insights that determines whether to monitor all access and throttled events or to track throttled events exclusively.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateContributorInsightsOutput) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "contributor_insights_status" in value:
        import aws_sdk_dynamodb.types.contributor_insights_status

        out["ContributorInsightsStatus"] = (
            aws_sdk_dynamodb.types.contributor_insights_status.serialize_aws_json_1_0(
                value["contributor_insights_status"]
            )
        )
    if "contributor_insights_mode" in value:
        import aws_sdk_dynamodb.types.contributor_insights_mode

        out["ContributorInsightsMode"] = (
            aws_sdk_dynamodb.types.contributor_insights_mode.serialize_aws_json_1_0(
                value["contributor_insights_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateContributorInsightsOutput:
    out: UpdateContributorInsightsOutput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "ContributorInsightsStatus" in data:
        import aws_sdk_dynamodb.types.contributor_insights_status

        out["contributor_insights_status"] = (
            aws_sdk_dynamodb.types.contributor_insights_status.deserialize_aws_json_1_0(
                data["ContributorInsightsStatus"]
            )
        )
    if "ContributorInsightsMode" in data:
        import aws_sdk_dynamodb.types.contributor_insights_mode

        out["contributor_insights_mode"] = (
            aws_sdk_dynamodb.types.contributor_insights_mode.deserialize_aws_json_1_0(
                data["ContributorInsightsMode"]
            )
        )
    return out
