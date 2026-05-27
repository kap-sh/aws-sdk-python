"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExecuteTransactionOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity_multiple
    import aws_sdk_dynamodb.types.item_response_list


class ExecuteTransactionOutput(TypedDict):
    responses: NotRequired["aws_sdk_dynamodb.types.item_response_list.ItemResponseList"]
    """<p>The response to a PartiQL transaction.</p>"""
    consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_multiple.ConsumedCapacityMultiple"
    ]
    """<p>The capacity units consumed by the entire operation. The values of the list are ordered according to the ordering of the statements.</p>"""
