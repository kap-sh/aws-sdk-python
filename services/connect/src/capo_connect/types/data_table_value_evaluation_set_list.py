"""Generated from Smithy shape ``com.amazonaws.connect#DataTableValueEvaluationSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.data_table_value_evaluation_set

DataTableValueEvaluationSetList: TypeAlias = list[
    "capo_connect.types.data_table_value_evaluation_set.DataTableValueEvaluationSet"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableValueEvaluationSetList) -> list:
    import capo_connect.types.data_table_value_evaluation_set

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.data_table_value_evaluation_set.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataTableValueEvaluationSetList:
    import capo_connect.types.data_table_value_evaluation_set

    out: DataTableValueEvaluationSetList = []
    for item in data:
        out.append(
            capo_connect.types.data_table_value_evaluation_set.deserialize_json(item)
        )
    return out
