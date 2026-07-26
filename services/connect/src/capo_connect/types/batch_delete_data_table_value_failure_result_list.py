"""Generated from Smithy shape ``com.amazonaws.connect#BatchDeleteDataTableValueFailureResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.batch_delete_data_table_value_failure_result

BatchDeleteDataTableValueFailureResultList: TypeAlias = list[
    "capo_connect.types.batch_delete_data_table_value_failure_result.BatchDeleteDataTableValueFailureResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDataTableValueFailureResultList) -> list:
    import capo_connect.types.batch_delete_data_table_value_failure_result

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.batch_delete_data_table_value_failure_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteDataTableValueFailureResultList:
    import capo_connect.types.batch_delete_data_table_value_failure_result

    out: BatchDeleteDataTableValueFailureResultList = []
    for item in data:
        out.append(
            capo_connect.types.batch_delete_data_table_value_failure_result.deserialize_json(
                item
            )
        )
    return out
