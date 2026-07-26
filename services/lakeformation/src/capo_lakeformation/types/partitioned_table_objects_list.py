"""Generated from Smithy shape ``com.amazonaws.lakeformation#PartitionedTableObjectsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.partition_objects

PartitionedTableObjectsList: TypeAlias = list[
    "capo_lakeformation.types.partition_objects.PartitionObjects"
]


# --- restJson1 ser/de ---
def serialize_json(value: PartitionedTableObjectsList) -> list:
    import capo_lakeformation.types.partition_objects

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.partition_objects.serialize_json(item))
    return out


def deserialize_json(data: list) -> PartitionedTableObjectsList:
    import capo_lakeformation.types.partition_objects

    out: PartitionedTableObjectsList = []
    for item in data:
        out.append(capo_lakeformation.types.partition_objects.deserialize_json(item))
    return out
