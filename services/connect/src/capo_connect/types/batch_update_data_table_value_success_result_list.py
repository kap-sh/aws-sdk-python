"""Generated from Smithy shape ``com.amazonaws.connect#BatchUpdateDataTableValueSuccessResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.batch_update_data_table_value_success_result

BatchUpdateDataTableValueSuccessResultList: TypeAlias = list[
    "capo_connect.types.batch_update_data_table_value_success_result.BatchUpdateDataTableValueSuccessResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDataTableValueSuccessResultList) -> list:
    import capo_connect.types.batch_update_data_table_value_success_result

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.batch_update_data_table_value_success_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateDataTableValueSuccessResultList:
    import capo_connect.types.batch_update_data_table_value_success_result

    out: BatchUpdateDataTableValueSuccessResultList = []
    for item in data:
        out.append(
            capo_connect.types.batch_update_data_table_value_success_result.deserialize_json(
                item
            )
        )
    return out
