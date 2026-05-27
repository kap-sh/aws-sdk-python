"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConsumedCapacity``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.capacity
    import aws_sdk_dynamodb.types.consumed_capacity_units
    import aws_sdk_dynamodb.types.secondary_indexes_capacity_map
    import aws_sdk_dynamodb.types.table_arn


class ConsumedCapacity(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p>The name of the table that was affected by the operation. If you had specified the Amazon Resource Name (ARN) of a table in the input, you'll see the table ARN in the response.</p>"""
    capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of capacity units consumed by the operation.</p>"""
    read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of read capacity units consumed by the operation.</p>"""
    write_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of write capacity units consumed by the operation.</p>"""
    table: NotRequired["aws_sdk_dynamodb.types.capacity.Capacity"]
    """<p>The amount of throughput consumed on the table affected by the operation.</p>"""
    local_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.secondary_indexes_capacity_map.SecondaryIndexesCapacityMap"
    ]
    """<p>The amount of throughput consumed on each local index affected by the operation.</p>"""
    global_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.secondary_indexes_capacity_map.SecondaryIndexesCapacityMap"
    ]
    """<p>The amount of throughput consumed on each global index affected by the operation.</p>"""
