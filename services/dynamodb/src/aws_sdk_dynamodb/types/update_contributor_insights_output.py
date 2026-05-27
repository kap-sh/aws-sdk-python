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
