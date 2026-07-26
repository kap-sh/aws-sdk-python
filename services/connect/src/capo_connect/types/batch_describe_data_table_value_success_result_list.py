"""Generated from Smithy shape ``com.amazonaws.connect#BatchDescribeDataTableValueSuccessResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.batch_describe_data_table_value_success_result

BatchDescribeDataTableValueSuccessResultList: TypeAlias = list[
    "capo_connect.types.batch_describe_data_table_value_success_result.BatchDescribeDataTableValueSuccessResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeDataTableValueSuccessResultList) -> list:
    import capo_connect.types.batch_describe_data_table_value_success_result

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.batch_describe_data_table_value_success_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDescribeDataTableValueSuccessResultList:
    import capo_connect.types.batch_describe_data_table_value_success_result

    out: BatchDescribeDataTableValueSuccessResultList = []
    for item in data:
        out.append(
            capo_connect.types.batch_describe_data_table_value_success_result.deserialize_json(
                item
            )
        )
    return out
