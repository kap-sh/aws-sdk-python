"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactGetItemsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.return_consumed_capacity
    import aws_sdk_dynamodb.types.transact_get_item_list


class TransactGetItemsInput(TypedDict):
    transact_items: "aws_sdk_dynamodb.types.transact_get_item_list.TransactGetItemList"
    """<p>An ordered array of up to 100 <code>TransactGetItem</code> objects, each of which contains a <code>Get</code> structure.</p>"""
    return_consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    """<p>A value of <code>TOTAL</code> causes consumed capacity information to be returned, and a value of <code>NONE</code> prevents that information from being returned. No other value is valid.</p>"""
