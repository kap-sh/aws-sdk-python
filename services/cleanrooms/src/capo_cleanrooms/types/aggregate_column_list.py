"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AggregateColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.aggregate_column

AggregateColumnList: TypeAlias = list[
    "capo_cleanrooms.types.aggregate_column.AggregateColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregateColumnList) -> list:
    import capo_cleanrooms.types.aggregate_column

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.aggregate_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregateColumnList:
    import capo_cleanrooms.types.aggregate_column

    out: AggregateColumnList = []
    for item in data:
        out.append(capo_cleanrooms.types.aggregate_column.deserialize_json(item))
    return out
