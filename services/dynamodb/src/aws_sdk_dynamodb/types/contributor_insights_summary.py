"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContributorInsightsSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.contributor_insights_mode
    import aws_sdk_dynamodb.types.contributor_insights_status
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.table_name


class ContributorInsightsSummary(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>Name of the table associated with the summary.</p>"""
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>Name of the index associated with the summary, if any.</p>"""
    contributor_insights_status: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_status.ContributorInsightsStatus"
    ]
    """<p>Describes the current status for contributor insights for the given table and index, if applicable.</p>"""
    contributor_insights_mode: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_mode.ContributorInsightsMode"
    ]
    """<p>Indicates the current mode of CloudWatch Contributor Insights, specifying whether it tracks all access and throttled events or throttled events only for the DynamoDB table or index.</p>"""
