"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeContinuousBackupsInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn


class DescribeContinuousBackupsInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>Name of the table for which the customer wants to check the continuous backups and point in time recovery settings.</p> <p>You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
