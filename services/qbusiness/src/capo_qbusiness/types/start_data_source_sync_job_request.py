"""Generated from Smithy shape ``com.amazonaws.qbusiness#StartDataSourceSyncJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.data_source_id
    import capo_qbusiness.types.index_id


class StartDataSourceSyncJobRequest(TypedDict, closed=True):
    data_source_id: "capo_qbusiness.types.data_source_id.DataSourceId"
    """<p> The identifier of the data source connector. </p>"""
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of Amazon Q Business application the data source is connected to.</p>"""
    index_id: "capo_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index used with the data source connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDataSourceSyncJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartDataSourceSyncJobRequest:
    out: StartDataSourceSyncJobRequest = {}  # type: ignore[typeddict-item]
    return out
