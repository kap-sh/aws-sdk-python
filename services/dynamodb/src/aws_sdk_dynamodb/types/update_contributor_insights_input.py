"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateContributorInsightsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.contributor_insights_action
    import aws_sdk_dynamodb.types.contributor_insights_mode
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.table_arn


class UpdateContributorInsightsInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The global secondary index name, if applicable.</p>"""
    contributor_insights_action: (
        "aws_sdk_dynamodb.types.contributor_insights_action.ContributorInsightsAction"
    )
    """<p>Represents the contributor insights action.</p>"""
    contributor_insights_mode: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_mode.ContributorInsightsMode"
    ]
    """<p>Specifies whether to track all access and throttled events or throttled events only for the DynamoDB table or index.</p>"""
