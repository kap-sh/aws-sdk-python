"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchExecuteStatementOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity_multiple
    import aws_sdk_dynamodb.types.parti_ql_batch_response


class BatchExecuteStatementOutput(TypedDict):
    responses: NotRequired[
        "aws_sdk_dynamodb.types.parti_ql_batch_response.PartiQLBatchResponse"
    ]
    """<p>The response to each PartiQL statement in the batch. The values of the list are ordered according to the ordering of the request statements.</p>"""
    consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_multiple.ConsumedCapacityMultiple"
    ]
    """<p>The capacity units consumed by the entire operation. The values of the list are ordered according to the ordering of the statements.</p>"""
