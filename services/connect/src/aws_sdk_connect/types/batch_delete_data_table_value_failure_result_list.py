"""Generated from Smithy shape ``com.amazonaws.connect#BatchDeleteDataTableValueFailureResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.batch_delete_data_table_value_failure_result

BatchDeleteDataTableValueFailureResultList: TypeAlias = list[
    "aws_sdk_connect.types.batch_delete_data_table_value_failure_result.BatchDeleteDataTableValueFailureResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDataTableValueFailureResultList) -> list:
    import aws_sdk_connect.types.batch_delete_data_table_value_failure_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.batch_delete_data_table_value_failure_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteDataTableValueFailureResultList:
    import aws_sdk_connect.types.batch_delete_data_table_value_failure_result

    out: BatchDeleteDataTableValueFailureResultList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.batch_delete_data_table_value_failure_result.deserialize_json(
                item
            )
        )
    return out
