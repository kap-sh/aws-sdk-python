"""Generated from Smithy shape ``com.amazonaws.keyspaces#PartitionKey``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.generic_string


class PartitionKey(TypedDict):
    name: "aws_sdk_keyspaces.types.generic_string.GenericString"
    """<p>The name(s) of the partition key column(s).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartitionKey) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PartitionKey:
    out: PartitionKey = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PartitionKey.name required")
    return out
