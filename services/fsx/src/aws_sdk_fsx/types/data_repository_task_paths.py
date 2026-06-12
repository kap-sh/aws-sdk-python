"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_task_path

DataRepositoryTaskPaths: TypeAlias = list[
    "aws_sdk_fsx.types.data_repository_task_path.DataRepositoryTaskPath"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskPaths) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DataRepositoryTaskPaths:
    return list(data)
