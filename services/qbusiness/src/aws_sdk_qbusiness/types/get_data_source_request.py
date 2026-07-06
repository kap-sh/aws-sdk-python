"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.index_id


class GetDataSourceRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identfier of the index used with the data source connector.</p>"""
    data_source_id: "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataSourceRequest:
    out: GetDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
