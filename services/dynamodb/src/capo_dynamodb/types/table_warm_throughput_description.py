"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableWarmThroughputDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.positive_long_object
    import capo_dynamodb.types.table_status


class TableWarmThroughputDescription(TypedDict, closed=True):
    read_units_per_second: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Represents the base table's warm throughput value in read units per second.</p>"""
    write_units_per_second: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Represents the base table's warm throughput value in write units per second.</p>"""
    status: NotRequired["capo_dynamodb.types.table_status.TableStatus"]
    """<p>Represents warm throughput value of the base table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableWarmThroughputDescription) -> dict:
    out: dict = {}
    if "read_units_per_second" in value:
        out["ReadUnitsPerSecond"] = value["read_units_per_second"]
    if "write_units_per_second" in value:
        out["WriteUnitsPerSecond"] = value["write_units_per_second"]
    if "status" in value:
        import capo_dynamodb.types.table_status

        out["Status"] = capo_dynamodb.types.table_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TableWarmThroughputDescription:
    out: TableWarmThroughputDescription = {}  # type: ignore[typeddict-item]
    if data.get("ReadUnitsPerSecond") is not None:
        out["read_units_per_second"] = data["ReadUnitsPerSecond"]
    if data.get("WriteUnitsPerSecond") is not None:
        out["write_units_per_second"] = data["WriteUnitsPerSecond"]
    if data.get("Status") is not None:
        import capo_dynamodb.types.table_status

        out["status"] = capo_dynamodb.types.table_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    return out
