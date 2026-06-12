"""Generated from Smithy shape ``com.amazonaws.kendra#StopDataSourceSyncJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_id
    import aws_sdk_kendra.types.index_id


class StopDataSourceSyncJobRequest(TypedDict):
    id: "aws_sdk_kendra.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source connector for which to stop the synchronization jobs.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index used with the data source connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopDataSourceSyncJobRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopDataSourceSyncJobRequest:
    out: StopDataSourceSyncJobRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("StopDataSourceSyncJobRequest.id required")
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("StopDataSourceSyncJobRequest.index_id required")
    return out
