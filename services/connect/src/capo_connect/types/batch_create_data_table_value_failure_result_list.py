"""Generated from Smithy shape ``com.amazonaws.connect#BatchCreateDataTableValueFailureResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.batch_create_data_table_value_failure_result

BatchCreateDataTableValueFailureResultList: TypeAlias = list[
    "capo_connect.types.batch_create_data_table_value_failure_result.BatchCreateDataTableValueFailureResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDataTableValueFailureResultList) -> list:
    import capo_connect.types.batch_create_data_table_value_failure_result

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.batch_create_data_table_value_failure_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateDataTableValueFailureResultList:
    import capo_connect.types.batch_create_data_table_value_failure_result

    out: BatchCreateDataTableValueFailureResultList = []
    for item in data:
        out.append(
            capo_connect.types.batch_create_data_table_value_failure_result.deserialize_json(
                item
            )
        )
    return out
