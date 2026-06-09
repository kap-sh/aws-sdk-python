"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableWarmThroughputDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.positive_long_object
    import aws_sdk_dynamodb.types.table_status


class TableWarmThroughputDescription(TypedDict):
    read_units_per_second: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Represents the base table's warm throughput value in read units per second.</p>"""
    write_units_per_second: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Represents the base table's warm throughput value in write units per second.</p>"""
    status: NotRequired["aws_sdk_dynamodb.types.table_status.TableStatus"]
    """<p>Represents warm throughput value of the base table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableWarmThroughputDescription) -> dict:
    out: dict = {}
    if "read_units_per_second" in value:
        out["ReadUnitsPerSecond"] = value["read_units_per_second"]
    if "write_units_per_second" in value:
        out["WriteUnitsPerSecond"] = value["write_units_per_second"]
    if "status" in value:
        import aws_sdk_dynamodb.types.table_status

        out["Status"] = aws_sdk_dynamodb.types.table_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TableWarmThroughputDescription:
    out: TableWarmThroughputDescription = {}  # type: ignore[typeddict-item]
    if "ReadUnitsPerSecond" in data:
        out["read_units_per_second"] = data["ReadUnitsPerSecond"]
    if "WriteUnitsPerSecond" in data:
        out["write_units_per_second"] = data["WriteUnitsPerSecond"]
    if "Status" in data:
        import aws_sdk_dynamodb.types.table_status

        out["status"] = aws_sdk_dynamodb.types.table_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    return out
