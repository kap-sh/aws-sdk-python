"""Generated from Smithy shape ``com.amazonaws.connect#BatchDeleteDataTableValueSuccessResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.batch_delete_data_table_value_success_result

BatchDeleteDataTableValueSuccessResultList: TypeAlias = list[
    "aws_sdk_connect.types.batch_delete_data_table_value_success_result.BatchDeleteDataTableValueSuccessResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDataTableValueSuccessResultList) -> list:
    import aws_sdk_connect.types.batch_delete_data_table_value_success_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.batch_delete_data_table_value_success_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteDataTableValueSuccessResultList:
    import aws_sdk_connect.types.batch_delete_data_table_value_success_result

    out: BatchDeleteDataTableValueSuccessResultList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.batch_delete_data_table_value_success_result.deserialize_json(
                item
            )
        )
    return out
