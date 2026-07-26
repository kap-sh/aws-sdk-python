"""Generated from Smithy shape ``com.amazonaws.connect#BatchUpdateDataTableValueFailureResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.batch_update_data_table_value_failure_result

BatchUpdateDataTableValueFailureResultList: TypeAlias = list[
    "capo_connect.types.batch_update_data_table_value_failure_result.BatchUpdateDataTableValueFailureResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDataTableValueFailureResultList) -> list:
    import capo_connect.types.batch_update_data_table_value_failure_result

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.batch_update_data_table_value_failure_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateDataTableValueFailureResultList:
    import capo_connect.types.batch_update_data_table_value_failure_result

    out: BatchUpdateDataTableValueFailureResultList = []
    for item in data:
        out.append(
            capo_connect.types.batch_update_data_table_value_failure_result.deserialize_json(
                item
            )
        )
    return out
