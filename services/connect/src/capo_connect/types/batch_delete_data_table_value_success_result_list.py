"""Generated from Smithy shape ``com.amazonaws.connect#BatchDeleteDataTableValueSuccessResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.batch_delete_data_table_value_success_result

BatchDeleteDataTableValueSuccessResultList: TypeAlias = list[
    "capo_connect.types.batch_delete_data_table_value_success_result.BatchDeleteDataTableValueSuccessResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDataTableValueSuccessResultList) -> list:
    import capo_connect.types.batch_delete_data_table_value_success_result

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.batch_delete_data_table_value_success_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteDataTableValueSuccessResultList:
    import capo_connect.types.batch_delete_data_table_value_success_result

    out: BatchDeleteDataTableValueSuccessResultList = []
    for item in data:
        out.append(
            capo_connect.types.batch_delete_data_table_value_success_result.deserialize_json(
                item
            )
        )
    return out
