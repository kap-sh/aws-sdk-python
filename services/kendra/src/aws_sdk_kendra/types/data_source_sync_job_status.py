"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceSyncJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

DataSourceSyncJobStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
    "SYNCING",
    "INCOMPLETE",
    "STOPPING",
    "ABORTED",
    "SYNCING_INDEXING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "SUCCEEDED",
        "SYNCING",
        "INCOMPLETE",
        "STOPPING",
        "ABORTED",
        "SYNCING_INDEXING",
    )
)


def serialize_aws_json_1_1(value: DataSourceSyncJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSourceSyncJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceSyncJobStatus value: {data!r}")
    return cast(DataSourceSyncJobStatus, data)
