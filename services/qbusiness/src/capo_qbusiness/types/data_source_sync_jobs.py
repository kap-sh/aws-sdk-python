"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceSyncJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.data_source_sync_job

DataSourceSyncJobs: TypeAlias = list[
    "capo_qbusiness.types.data_source_sync_job.DataSourceSyncJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSyncJobs) -> list:
    import capo_qbusiness.types.data_source_sync_job

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.data_source_sync_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceSyncJobs:
    import capo_qbusiness.types.data_source_sync_job

    out: DataSourceSyncJobs = []
    for item in data:
        out.append(capo_qbusiness.types.data_source_sync_job.deserialize_json(item))
    return out
