"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeGlobalTableInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_name


class DescribeGlobalTableInput(TypedDict):
    global_table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The name of the global table.</p>"""
