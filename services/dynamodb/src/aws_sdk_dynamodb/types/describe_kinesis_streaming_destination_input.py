"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeKinesisStreamingDestinationInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn


class DescribeKinesisStreamingDestinationInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table being described. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
