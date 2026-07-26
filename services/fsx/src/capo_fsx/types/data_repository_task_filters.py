"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.data_repository_task_filter

DataRepositoryTaskFilters: TypeAlias = list[
    "capo_fsx.types.data_repository_task_filter.DataRepositoryTaskFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskFilters) -> list:
    import capo_fsx.types.data_repository_task_filter

    out: list = []
    for item in value:
        out.append(
            capo_fsx.types.data_repository_task_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataRepositoryTaskFilters:
    import capo_fsx.types.data_repository_task_filter

    out: DataRepositoryTaskFilters = []
    for item in data:
        out.append(
            capo_fsx.types.data_repository_task_filter.deserialize_aws_json_1_1(item)
        )
    return out
