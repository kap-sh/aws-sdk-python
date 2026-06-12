"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

DataRepositoryTaskType: TypeAlias = Literal[
    "EXPORT_TO_REPOSITORY",
    "IMPORT_METADATA_FROM_REPOSITORY",
    "RELEASE_DATA_FROM_FILESYSTEM",
    "AUTO_RELEASE_DATA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXPORT_TO_REPOSITORY",
        "IMPORT_METADATA_FROM_REPOSITORY",
        "RELEASE_DATA_FROM_FILESYSTEM",
        "AUTO_RELEASE_DATA",
    )
)


def serialize_aws_json_1_1(value: DataRepositoryTaskType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataRepositoryTaskType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataRepositoryTaskType value: {data!r}")
    return cast(DataRepositoryTaskType, data)
