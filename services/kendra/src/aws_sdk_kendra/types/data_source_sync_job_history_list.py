"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceSyncJobHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_sync_job

DataSourceSyncJobHistoryList: TypeAlias = list[
    "aws_sdk_kendra.types.data_source_sync_job.DataSourceSyncJob"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceSyncJobHistoryList) -> list:
    import aws_sdk_kendra.types.data_source_sync_job

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.data_source_sync_job.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataSourceSyncJobHistoryList:
    import aws_sdk_kendra.types.data_source_sync_job

    out: DataSourceSyncJobHistoryList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.data_source_sync_job.deserialize_aws_json_1_1(item)
        )
    return out
