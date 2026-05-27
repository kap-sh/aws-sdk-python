"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeTableOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_description


class DescribeTableOutput(TypedDict):
    table: NotRequired["aws_sdk_dynamodb.types.table_description.TableDescription"]
    """<p>The properties of the table.</p>"""
