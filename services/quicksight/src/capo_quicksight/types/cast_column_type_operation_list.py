"""Generated from Smithy shape ``com.amazonaws.quicksight#CastColumnTypeOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.cast_column_type_operation

CastColumnTypeOperationList: TypeAlias = list[
    "capo_quicksight.types.cast_column_type_operation.CastColumnTypeOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: CastColumnTypeOperationList) -> list:
    import capo_quicksight.types.cast_column_type_operation

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.cast_column_type_operation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CastColumnTypeOperationList:
    import capo_quicksight.types.cast_column_type_operation

    out: CastColumnTypeOperationList = []
    for item in data:
        out.append(
            capo_quicksight.types.cast_column_type_operation.deserialize_json(item)
        )
    return out
