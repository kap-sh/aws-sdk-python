"""Generated from Smithy shape ``com.amazonaws.qbusiness#StopDataSourceSyncJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.index_id


class StopDataSourceSyncJobRequest(TypedDict):
    data_source_id: "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
    """<p> The identifier of the data source connector. </p>"""
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application that the data source is connected to.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index used with the Amazon Q Business data source connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopDataSourceSyncJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopDataSourceSyncJobRequest:
    out: StopDataSourceSyncJobRequest = {}  # type: ignore[typeddict-item]
    return out
