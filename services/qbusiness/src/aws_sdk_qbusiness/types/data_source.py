"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.data_source_name
    import aws_sdk_qbusiness.types.data_source_status
    import aws_sdk_qbusiness.types.string
    import aws_sdk_qbusiness.types.timestamp


class DataSource(TypedDict, closed=True):
    display_name: NotRequired["aws_sdk_qbusiness.types.data_source_name.DataSourceName"]
    """<p>The name of the Amazon Q Business data source.</p>"""
    data_source_id: NotRequired["aws_sdk_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the Amazon Q Business data source.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The type of the Amazon Q Business data source.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business data source was created.</p>"""
    updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business data source was last updated. </p>"""
    status: NotRequired["aws_sdk_qbusiness.types.data_source_status.DataSourceStatus"]
    """<p>The status of the Amazon Q Business data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSource) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "data_source_id" in value:
        out["dataSourceId"] = value["data_source_id"]
    if "type" in value:
        out["type"] = value["type"]
    if "created_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["createdAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["updatedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "status" in value:
        import aws_sdk_qbusiness.types.data_source_status

        out["status"] = aws_sdk_qbusiness.types.data_source_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    if "type" in data:
        out["type"] = data["type"]
    if "createdAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["created_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["updated_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "status" in data:
        import aws_sdk_qbusiness.types.data_source_status

        out["status"] = aws_sdk_qbusiness.types.data_source_status.deserialize_json(
            data["status"]
        )
    return out
