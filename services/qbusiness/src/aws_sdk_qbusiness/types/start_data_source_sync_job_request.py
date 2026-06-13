"""Generated from Smithy shape ``com.amazonaws.qbusiness#StartDataSourceSyncJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.index_id


class StartDataSourceSyncJobRequest(TypedDict):
    data_source_id: "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
    """<p> The identifier of the data source connector. </p>"""
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of Amazon Q Business application the data source is connected to.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index used with the data source connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDataSourceSyncJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartDataSourceSyncJobRequest:
    out: StartDataSourceSyncJobRequest = {}  # type: ignore[typeddict-item]
    return out
