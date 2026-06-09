"""Generated from Smithy shape ``com.amazonaws.dynamodb#WarmThroughput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.long_object


class WarmThroughput(TypedDict):
    read_units_per_second: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>Represents the number of read operations your base table can instantaneously support.</p>"""
    write_units_per_second: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>Represents the number of write operations your base table can instantaneously support.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WarmThroughput) -> dict:
    out: dict = {}
    if "read_units_per_second" in value:
        out["ReadUnitsPerSecond"] = value["read_units_per_second"]
    if "write_units_per_second" in value:
        out["WriteUnitsPerSecond"] = value["write_units_per_second"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WarmThroughput:
    out: WarmThroughput = {}  # type: ignore[typeddict-item]
    if "ReadUnitsPerSecond" in data:
        out["read_units_per_second"] = data["ReadUnitsPerSecond"]
    if "WriteUnitsPerSecond" in data:
        out["write_units_per_second"] = data["WriteUnitsPerSecond"]
    return out
