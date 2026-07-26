"""Generated from Smithy shape ``com.amazonaws.connect#DataTableEvaluatedValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.data_table_evaluated_value

DataTableEvaluatedValueList: TypeAlias = list[
    "capo_connect.types.data_table_evaluated_value.DataTableEvaluatedValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableEvaluatedValueList) -> list:
    import capo_connect.types.data_table_evaluated_value

    out: list = []
    for item in value:
        out.append(capo_connect.types.data_table_evaluated_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataTableEvaluatedValueList:
    import capo_connect.types.data_table_evaluated_value

    out: DataTableEvaluatedValueList = []
    for item in data:
        out.append(capo_connect.types.data_table_evaluated_value.deserialize_json(item))
    return out
