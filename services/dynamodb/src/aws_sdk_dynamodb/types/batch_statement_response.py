"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchStatementResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map
    import aws_sdk_dynamodb.types.batch_statement_error
    import aws_sdk_dynamodb.types.table_name


class BatchStatementResponse(TypedDict):
    error: NotRequired[
        "aws_sdk_dynamodb.types.batch_statement_error.BatchStatementError"
    ]
    """<p> The error associated with a failed PartiQL batch statement. </p>"""
    table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p> The table name associated with a failed PartiQL batch statement. </p>"""
    item: NotRequired["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
    """<p> A DynamoDB item associated with a BatchStatementResponse </p>"""
