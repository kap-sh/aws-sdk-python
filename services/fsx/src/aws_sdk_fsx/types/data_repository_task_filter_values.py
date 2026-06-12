"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_task_filter_value

DataRepositoryTaskFilterValues: TypeAlias = list[
    "aws_sdk_fsx.types.data_repository_task_filter_value.DataRepositoryTaskFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DataRepositoryTaskFilterValues:
    return list(data)
