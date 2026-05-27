"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactGetItemsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity_multiple
    import aws_sdk_dynamodb.types.item_response_list


class TransactGetItemsOutput(TypedDict):
    consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_multiple.ConsumedCapacityMultiple"
    ]
    """<p>If the <i>ReturnConsumedCapacity</i> value was <code>TOTAL</code>, this is an array of <code>ConsumedCapacity</code> objects, one for each table addressed by <code>TransactGetItem</code> objects in the <i>TransactItems</i> parameter. These <code>ConsumedCapacity</code> objects report the read-capacity units consumed by the <code>TransactGetItems</code> call in that table.</p>"""
    responses: NotRequired["aws_sdk_dynamodb.types.item_response_list.ItemResponseList"]
    """<p>An ordered array of up to 100 <code>ItemResponse</code> objects, each of which corresponds to the <code>TransactGetItem</code> object in the same position in the <i>TransactItems</i> array. Each <code>ItemResponse</code> object contains a Map of the name-value pairs that are the projected attributes of the requested item.</p> <p>If a requested item could not be retrieved, the corresponding <code>ItemResponse</code> object is Null, or if the requested item has no projected attributes, the corresponding <code>ItemResponse</code> object is an empty Map. </p>"""
