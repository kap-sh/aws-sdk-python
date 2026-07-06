"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.index_id


class DeleteDataSourceRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application used with the data source connector.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index used with the data source connector.</p>"""
    data_source_id: "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source connector that you want to delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataSourceRequest:
    out: DeleteDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
