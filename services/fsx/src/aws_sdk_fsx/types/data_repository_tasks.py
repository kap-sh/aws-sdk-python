"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_task

DataRepositoryTasks: TypeAlias = list[
    "aws_sdk_fsx.types.data_repository_task.DataRepositoryTask"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTasks) -> list:
    import aws_sdk_fsx.types.data_repository_task

    out: list = []
    for item in value:
        out.append(aws_sdk_fsx.types.data_repository_task.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataRepositoryTasks:
    import aws_sdk_fsx.types.data_repository_task

    out: DataRepositoryTasks = []
    for item in data:
        out.append(
            aws_sdk_fsx.types.data_repository_task.deserialize_aws_json_1_1(item)
        )
    return out
