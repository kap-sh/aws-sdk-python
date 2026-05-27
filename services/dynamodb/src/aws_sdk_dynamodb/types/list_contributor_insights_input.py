"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListContributorInsightsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.list_contributor_insights_limit
    import aws_sdk_dynamodb.types.next_token_string
    import aws_sdk_dynamodb.types.table_arn


class ListContributorInsightsInput(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    next_token: NotRequired["aws_sdk_dynamodb.types.next_token_string.NextTokenString"]
    """<p>A token to for the desired page, if there is one.</p>"""
    max_results: "aws_sdk_dynamodb.types.list_contributor_insights_limit.ListContributorInsightsLimit"
    """<p>Maximum number of results to return per page.</p>"""
