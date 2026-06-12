"""Generated from Smithy shape ``com.amazonaws.connect#BatchDescribeDataTableValueFailureResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.batch_describe_data_table_value_failure_result

BatchDescribeDataTableValueFailureResultList: TypeAlias = list[
    "aws_sdk_connect.types.batch_describe_data_table_value_failure_result.BatchDescribeDataTableValueFailureResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeDataTableValueFailureResultList) -> list:
    import aws_sdk_connect.types.batch_describe_data_table_value_failure_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.batch_describe_data_table_value_failure_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDescribeDataTableValueFailureResultList:
    import aws_sdk_connect.types.batch_describe_data_table_value_failure_result

    out: BatchDescribeDataTableValueFailureResultList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.batch_describe_data_table_value_failure_result.deserialize_json(
                item
            )
        )
    return out
