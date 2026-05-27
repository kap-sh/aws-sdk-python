"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListGlobalTablesOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_table_list
    import aws_sdk_dynamodb.types.table_name


class ListGlobalTablesOutput(TypedDict):
    global_tables: NotRequired[
        "aws_sdk_dynamodb.types.global_table_list.GlobalTableList"
    ]
    """<p>List of global table names.</p>"""
    last_evaluated_global_table_name: NotRequired[
        "aws_sdk_dynamodb.types.table_name.TableName"
    ]
    """<p>Last evaluated global table name.</p>"""
