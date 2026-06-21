"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceSyncJobStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: DataSourceSyncJobStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceSyncJobStatus:
    return cast(DataSourceSyncJobStatus, data)
