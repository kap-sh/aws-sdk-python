"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexWarmThroughputDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.index_status
    import capo_dynamodb.types.positive_long_object


class GlobalSecondaryIndexWarmThroughputDescription(TypedDict, closed=True):
    read_units_per_second: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Represents warm throughput read units per second value for a global secondary index.</p>"""
    write_units_per_second: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Represents warm throughput write units per second value for a global secondary index.</p>"""
    status: NotRequired["capo_dynamodb.types.index_status.IndexStatus"]
    """<p>Represents the warm throughput status being created or updated on a global secondary index. The status can only be <code>UPDATING</code> or <code>ACTIVE</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: GlobalSecondaryIndexWarmThroughputDescription,
) -> dict:
    out: dict = {}
    if "read_units_per_second" in value:
        out["ReadUnitsPerSecond"] = value["read_units_per_second"]
    if "write_units_per_second" in value:
        out["WriteUnitsPerSecond"] = value["write_units_per_second"]
    if "status" in value:
        import capo_dynamodb.types.index_status

        out["Status"] = capo_dynamodb.types.index_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GlobalSecondaryIndexWarmThroughputDescription:
    out: GlobalSecondaryIndexWarmThroughputDescription = {}  # type: ignore[typeddict-item]
    if data.get("ReadUnitsPerSecond") is not None:
        out["read_units_per_second"] = data["ReadUnitsPerSecond"]
    if data.get("WriteUnitsPerSecond") is not None:
        out["write_units_per_second"] = data["WriteUnitsPerSecond"]
    if data.get("Status") is not None:
        import capo_dynamodb.types.index_status

        out["status"] = capo_dynamodb.types.index_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    return out
