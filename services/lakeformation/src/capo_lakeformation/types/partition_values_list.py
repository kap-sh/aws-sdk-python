"""Generated from Smithy shape ``com.amazonaws.lakeformation#PartitionValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.partition_value_string

PartitionValuesList: TypeAlias = list[
    "capo_lakeformation.types.partition_value_string.PartitionValueString"
]


# --- restJson1 ser/de ---
def serialize_json(value: PartitionValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> PartitionValuesList:
    return list(data)
