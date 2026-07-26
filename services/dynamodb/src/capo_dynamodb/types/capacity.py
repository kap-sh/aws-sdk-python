"""Generated from Smithy shape ``com.amazonaws.dynamodb#Capacity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.consumed_capacity_units


class Capacity(TypedDict, closed=True):
    read_capacity_units: NotRequired[
        "capo_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of read capacity units consumed on a table or an index.</p>"""
    write_capacity_units: NotRequired[
        "capo_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of write capacity units consumed on a table or an index.</p>"""
    capacity_units: NotRequired[
        "capo_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The total number of capacity units consumed on a table or an index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Capacity) -> dict:
    out: dict = {}
    if "read_capacity_units" in value:
        out["ReadCapacityUnits"] = value["read_capacity_units"]
    if "write_capacity_units" in value:
        out["WriteCapacityUnits"] = value["write_capacity_units"]
    if "capacity_units" in value:
        out["CapacityUnits"] = value["capacity_units"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Capacity:
    out: Capacity = {}  # type: ignore[typeddict-item]
    if "ReadCapacityUnits" in data:
        out["read_capacity_units"] = data["ReadCapacityUnits"]
    if "WriteCapacityUnits" in data:
        out["write_capacity_units"] = data["WriteCapacityUnits"]
    if "CapacityUnits" in data:
        out["capacity_units"] = data["CapacityUnits"]
    return out
