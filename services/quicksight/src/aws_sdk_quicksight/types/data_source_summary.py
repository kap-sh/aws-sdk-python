"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.data_source_type
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.resource_name
    import aws_sdk_quicksight.types.timestamp


class DataSourceSummary(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The arn of the datasource.</p>"""
    data_source_id: NotRequired["aws_sdk_quicksight.types.resource_id.ResourceId"]
    """<p>The unique ID of the data source.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.resource_name.ResourceName"]
    """<p>The name of the data source.</p>"""
    type: NotRequired["aws_sdk_quicksight.types.data_source_type.DataSourceType"]
    """<p>The type of the data source.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time that the data source was created. This value is expressed in MM-DD-YYYY HH:MM:SS format.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time the data source was last updated. This value is expressed in MM-DD-YYYY HH:MM:SS format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_quicksight.types.data_source_type

        out["Type"] = aws_sdk_quicksight.types.data_source_type.serialize_json(
            value["type"]
        )
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> DataSourceSummary:
    out: DataSourceSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_quicksight.types.data_source_type

        out["type"] = aws_sdk_quicksight.types.data_source_type.deserialize_json(
            data["Type"]
        )
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    return out
