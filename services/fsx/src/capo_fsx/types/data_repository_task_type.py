"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskType``."""

from typing import Literal, TypeAlias, cast

DataRepositoryTaskType: TypeAlias = Literal[
    "EXPORT_TO_REPOSITORY",
    "IMPORT_METADATA_FROM_REPOSITORY",
    "RELEASE_DATA_FROM_FILESYSTEM",
    "AUTO_RELEASE_DATA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataRepositoryTaskType:
    return cast(DataRepositoryTaskType, data)
