"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskFilterName``."""

from typing import Literal, TypeAlias, cast

DataRepositoryTaskFilterName: TypeAlias = Literal[
    "file-system-id",
    "task-lifecycle",
    "data-repository-association-id",
    "file-cache-id",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataRepositoryTaskFilterName:
    return cast(DataRepositoryTaskFilterName, data)
