"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

DataRepositoryTaskFilterName: TypeAlias = Literal[
    "file-system-id",
    "task-lifecycle",
    "data-repository-association-id",
    "file-cache-id",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "file-system-id",
        "task-lifecycle",
        "data-repository-association-id",
        "file-cache-id",
    )
)


def serialize_aws_json_1_1(value: DataRepositoryTaskFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataRepositoryTaskFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataRepositoryTaskFilterName value: {data!r}"
        )
    return cast(DataRepositoryTaskFilterName, data)
