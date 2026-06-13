"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceSyncJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

DataSourceSyncJobStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
    "SYNCING",
    "INCOMPLETE",
    "STOPPING",
    "ABORTED",
    "SYNCING_INDEXING",
]


# --- restJson1 ser/de ---
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


def serialize_json(value: DataSourceSyncJobStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceSyncJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceSyncJobStatus value: {data!r}")
    return cast(DataSourceSyncJobStatus, data)
