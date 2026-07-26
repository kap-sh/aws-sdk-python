"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataPartitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.data_partition

DataPartitions: TypeAlias = list["capo_iotfleetwise.types.data_partition.DataPartition"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataPartitions) -> list:
    import capo_iotfleetwise.types.data_partition

    out: list = []
    for item in value:
        out.append(capo_iotfleetwise.types.data_partition.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DataPartitions:
    import capo_iotfleetwise.types.data_partition

    out: DataPartitions = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.data_partition.deserialize_aws_json_1_0(item)
        )
    return out
