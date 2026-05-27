"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListTablesInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.list_tables_input_limit
    import aws_sdk_dynamodb.types.table_name


class ListTablesInput(TypedDict):
    exclusive_start_table_name: NotRequired[
        "aws_sdk_dynamodb.types.table_name.TableName"
    ]
    """<p>The first table name that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedTableName</code> in a previous operation, so that you can obtain the next page of results.</p>"""
    limit: NotRequired[
        "aws_sdk_dynamodb.types.list_tables_input_limit.ListTablesInputLimit"
    ]
    """<p>A maximum number of table names to return. If this parameter is not specified, the limit is 100.</p>"""
