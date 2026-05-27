"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteTableInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn


class DeleteTableInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to delete. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
