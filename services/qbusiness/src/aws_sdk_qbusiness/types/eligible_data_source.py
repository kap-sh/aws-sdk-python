"""Generated from Smithy shape ``com.amazonaws.qbusiness#EligibleDataSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.index_id


class EligibleDataSource(TypedDict):
    index_id: NotRequired["aws_sdk_qbusiness.types.index_id.IndexId"]
    """<p>The identifier of the index the data source is attached to.</p>"""
    data_source_id: NotRequired["aws_sdk_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EligibleDataSource) -> dict:
    out: dict = {}
    if "index_id" in value:
        out["indexId"] = value["index_id"]
    if "data_source_id" in value:
        out["dataSourceId"] = value["data_source_id"]
    return out


def deserialize_json(data: dict) -> EligibleDataSource:
    out: EligibleDataSource = {}  # type: ignore[typeddict-item]
    if "indexId" in data:
        out["index_id"] = data["indexId"]
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    return out
