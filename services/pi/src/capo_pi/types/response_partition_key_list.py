"""Generated from Smithy shape ``com.amazonaws.pi#ResponsePartitionKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.response_partition_key

ResponsePartitionKeyList: TypeAlias = list[
    "capo_pi.types.response_partition_key.ResponsePartitionKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponsePartitionKeyList) -> list:
    import capo_pi.types.response_partition_key

    out: list = []
    for item in value:
        out.append(capo_pi.types.response_partition_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResponsePartitionKeyList:
    import capo_pi.types.response_partition_key

    out: ResponsePartitionKeyList = []
    for item in data:
        out.append(capo_pi.types.response_partition_key.deserialize_aws_json_1_1(item))
    return out
