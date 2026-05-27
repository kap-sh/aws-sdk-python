"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchStatementError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map
    import aws_sdk_dynamodb.types.batch_statement_error_code_enum
    import aws_sdk_dynamodb.types.string


class BatchStatementError(TypedDict):
    code: NotRequired[
        "aws_sdk_dynamodb.types.batch_statement_error_code_enum.BatchStatementErrorCodeEnum"
    ]
    """<p> The error code associated with the failed PartiQL batch statement. </p>"""
    message: NotRequired["aws_sdk_dynamodb.types.string.String"]
    """<p> The error message associated with the PartiQL batch response. </p>"""
    item: NotRequired["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
    """<p>The item which caused the condition check to fail. This will be set if ReturnValuesOnConditionCheckFailure is specified as <code>ALL_OLD</code>.</p>"""
