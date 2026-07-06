"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PartitionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.partition_key_name
    import aws_sdk_cloudtrail.types.partition_key_type


class PartitionKey(TypedDict, closed=True):
    name: "aws_sdk_cloudtrail.types.partition_key_name.PartitionKeyName"
    """<p>The name of the partition key.</p>"""
    type: "aws_sdk_cloudtrail.types.partition_key_type.PartitionKeyType"
    """<p>The data type of the partition key. For example, <code>bigint</code> or <code>string</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionKey) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionKey:
    out: PartitionKey = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PartitionKey.name required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("PartitionKey.type required")
    return out
