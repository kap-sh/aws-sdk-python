"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeTimeToLiveInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn


class DescribeTimeToLiveInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to be described. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
