"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceSyncJobStatus``."""

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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceSyncJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSourceSyncJobStatus:
    return cast(DataSourceSyncJobStatus, data)
