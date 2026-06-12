"""Generated from Smithy shape ``com.amazonaws.connect#BatchUpdateDataTableValueFailureResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.batch_update_data_table_value_failure_result

BatchUpdateDataTableValueFailureResultList: TypeAlias = list[
    "aws_sdk_connect.types.batch_update_data_table_value_failure_result.BatchUpdateDataTableValueFailureResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDataTableValueFailureResultList) -> list:
    import aws_sdk_connect.types.batch_update_data_table_value_failure_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.batch_update_data_table_value_failure_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateDataTableValueFailureResultList:
    import aws_sdk_connect.types.batch_update_data_table_value_failure_result

    out: BatchUpdateDataTableValueFailureResultList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.batch_update_data_table_value_failure_result.deserialize_json(
                item
            )
        )
    return out
