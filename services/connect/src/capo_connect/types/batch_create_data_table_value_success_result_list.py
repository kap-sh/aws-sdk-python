"""Generated from Smithy shape ``com.amazonaws.connect#BatchCreateDataTableValueSuccessResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.batch_create_data_table_value_success_result

BatchCreateDataTableValueSuccessResultList: TypeAlias = list[
    "capo_connect.types.batch_create_data_table_value_success_result.BatchCreateDataTableValueSuccessResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDataTableValueSuccessResultList) -> list:
    import capo_connect.types.batch_create_data_table_value_success_result

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.batch_create_data_table_value_success_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateDataTableValueSuccessResultList:
    import capo_connect.types.batch_create_data_table_value_success_result

    out: BatchCreateDataTableValueSuccessResultList = []
    for item in data:
        out.append(
            capo_connect.types.batch_create_data_table_value_success_result.deserialize_json(
                item
            )
        )
    return out
