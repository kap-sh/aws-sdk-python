"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListGlobalTablesInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.positive_integer_object
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.table_name


class ListGlobalTablesInput(TypedDict):
    exclusive_start_global_table_name: NotRequired[
        "aws_sdk_dynamodb.types.table_name.TableName"
    ]
    """<p>The first global table name that this operation will evaluate.</p>"""
    limit: NotRequired[
        "aws_sdk_dynamodb.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The maximum number of table names to return, if the parameter is not specified DynamoDB defaults to 100.</p> <p>If the number of global tables DynamoDB finds reaches this limit, it stops the operation and returns the table names collected up to that point, with a table name in the <code>LastEvaluatedGlobalTableName</code> to apply in a subsequent operation to the <code>ExclusiveStartGlobalTableName</code> parameter.</p>"""
    region_name: NotRequired["aws_sdk_dynamodb.types.region_name.RegionName"]
    """<p>Lists the global tables in a specific Region.</p>"""
