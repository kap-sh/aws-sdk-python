"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchExecuteStatementInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.parti_ql_batch_request
    import aws_sdk_dynamodb.types.return_consumed_capacity


class BatchExecuteStatementInput(TypedDict):
    statements: "aws_sdk_dynamodb.types.parti_ql_batch_request.PartiQLBatchRequest"
    """<p>The list of PartiQL statements representing the batch to run.</p>"""
    return_consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
