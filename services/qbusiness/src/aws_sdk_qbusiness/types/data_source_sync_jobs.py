"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceSyncJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.data_source_sync_job

DataSourceSyncJobs: TypeAlias = list[
    "aws_sdk_qbusiness.types.data_source_sync_job.DataSourceSyncJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSyncJobs) -> list:
    import aws_sdk_qbusiness.types.data_source_sync_job

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.data_source_sync_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceSyncJobs:
    import aws_sdk_qbusiness.types.data_source_sync_job

    out: DataSourceSyncJobs = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.data_source_sync_job.deserialize_json(item))
    return out
