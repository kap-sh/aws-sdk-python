"""Generated from Smithy shape ``com.amazonaws.keyspaces#PartitionKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.partition_key

PartitionKeyList: TypeAlias = list["capo_keyspaces.types.partition_key.PartitionKey"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartitionKeyList) -> list:
    import capo_keyspaces.types.partition_key

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.partition_key.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> PartitionKeyList:
    import capo_keyspaces.types.partition_key

    out: PartitionKeyList = []
    for item in data:
        out.append(capo_keyspaces.types.partition_key.deserialize_aws_json_1_0(item))
    return out
