"""Generated from Smithy shape ``com.amazonaws.dynamodb#Capacity``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity_units


class Capacity(TypedDict):
    read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of read capacity units consumed on a table or an index.</p>"""
    write_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of write capacity units consumed on a table or an index.</p>"""
    capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of capacity units consumed on a table or an index.</p>"""
