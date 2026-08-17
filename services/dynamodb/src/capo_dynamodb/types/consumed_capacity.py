"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConsumedCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.capacity
    import capo_dynamodb.types.consumed_capacity_units
    import capo_dynamodb.types.secondary_indexes_capacity_map
    import capo_dynamodb.types.table_arn


class ConsumedCapacity(TypedDict, closed=True):
    table_name: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p>The name of the table that was affected by the operation. If you had specified the Amazon Resource Name (ARN) of a table in the input, you'll see the table ARN in the response.</p>"""
    capacity_units: NotRequired[
        "capo_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of capacity units consumed by the operation.</p>"""
    read_capacity_units: NotRequired[
        "capo_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of read capacity units consumed by the operation.</p>"""
    write_capacity_units: NotRequired[
        "capo_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of write capacity units consumed by the operation.</p>"""
    table: NotRequired["capo_dynamodb.types.capacity.Capacity"]
    """<p>The amount of throughput consumed on the table affected by the operation.</p>"""
    local_secondary_indexes: NotRequired[
        "capo_dynamodb.types.secondary_indexes_capacity_map.SecondaryIndexesCapacityMap"
    ]
    """<p>The amount of throughput consumed on each local index affected by the operation.</p>"""
    global_secondary_indexes: NotRequired[
        "capo_dynamodb.types.secondary_indexes_capacity_map.SecondaryIndexesCapacityMap"
    ]
    """<p>The amount of throughput consumed on each global index affected by the operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConsumedCapacity) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "capacity_units" in value:
        out["CapacityUnits"] = value["capacity_units"]
    if "read_capacity_units" in value:
        out["ReadCapacityUnits"] = value["read_capacity_units"]
    if "write_capacity_units" in value:
        out["WriteCapacityUnits"] = value["write_capacity_units"]
    if "table" in value:
        import capo_dynamodb.types.capacity

        out["Table"] = capo_dynamodb.types.capacity.serialize_aws_json_1_0(
            value["table"]
        )
    if "local_secondary_indexes" in value:
        import capo_dynamodb.types.secondary_indexes_capacity_map

        out["LocalSecondaryIndexes"] = (
            capo_dynamodb.types.secondary_indexes_capacity_map.serialize_aws_json_1_0(
                value["local_secondary_indexes"]
            )
        )
    if "global_secondary_indexes" in value:
        import capo_dynamodb.types.secondary_indexes_capacity_map

        out["GlobalSecondaryIndexes"] = (
            capo_dynamodb.types.secondary_indexes_capacity_map.serialize_aws_json_1_0(
                value["global_secondary_indexes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConsumedCapacity:
    out: ConsumedCapacity = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("CapacityUnits") is not None:
        out["capacity_units"] = data["CapacityUnits"]
    if data.get("ReadCapacityUnits") is not None:
        out["read_capacity_units"] = data["ReadCapacityUnits"]
    if data.get("WriteCapacityUnits") is not None:
        out["write_capacity_units"] = data["WriteCapacityUnits"]
    if data.get("Table") is not None:
        import capo_dynamodb.types.capacity

        out["table"] = capo_dynamodb.types.capacity.deserialize_aws_json_1_0(
            data["Table"]
        )
    if data.get("LocalSecondaryIndexes") is not None:
        import capo_dynamodb.types.secondary_indexes_capacity_map

        out["local_secondary_indexes"] = (
            capo_dynamodb.types.secondary_indexes_capacity_map.deserialize_aws_json_1_0(
                data["LocalSecondaryIndexes"]
            )
        )
    if data.get("GlobalSecondaryIndexes") is not None:
        import capo_dynamodb.types.secondary_indexes_capacity_map

        out["global_secondary_indexes"] = (
            capo_dynamodb.types.secondary_indexes_capacity_map.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexes"]
            )
        )
    return out
