"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.data_repository_task

DataRepositoryTasks: TypeAlias = list[
    "capo_fsx.types.data_repository_task.DataRepositoryTask"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTasks) -> list:
    import capo_fsx.types.data_repository_task

    out: list = []
    for item in value:
        out.append(capo_fsx.types.data_repository_task.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataRepositoryTasks:
    import capo_fsx.types.data_repository_task

    out: DataRepositoryTasks = []
    for item in data:
        out.append(capo_fsx.types.data_repository_task.deserialize_aws_json_1_1(item))
    return out
