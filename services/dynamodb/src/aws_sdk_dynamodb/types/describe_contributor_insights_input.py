"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeContributorInsightsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.table_arn


class DescribeContributorInsightsInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to describe. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index to describe, if applicable.</p>"""
