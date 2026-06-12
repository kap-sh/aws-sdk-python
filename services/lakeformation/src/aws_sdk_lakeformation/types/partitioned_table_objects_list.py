"""Generated from Smithy shape ``com.amazonaws.lakeformation#PartitionedTableObjectsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.partition_objects

PartitionedTableObjectsList: TypeAlias = list[
    "aws_sdk_lakeformation.types.partition_objects.PartitionObjects"
]


# --- restJson1 ser/de ---
def serialize_json(value: PartitionedTableObjectsList) -> list:
    import aws_sdk_lakeformation.types.partition_objects

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.partition_objects.serialize_json(item))
    return out


def deserialize_json(data: list) -> PartitionedTableObjectsList:
    import aws_sdk_lakeformation.types.partition_objects

    out: PartitionedTableObjectsList = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.partition_objects.deserialize_json(item))
    return out
