"""Generated from Smithy shape ``com.amazonaws.opensearch#GetDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.data_source_description
    import aws_sdk_opensearch.types.data_source_name
    import aws_sdk_opensearch.types.data_source_status
    import aws_sdk_opensearch.types.data_source_type


class GetDataSourceResponse(TypedDict):
    data_source_type: NotRequired[
        "aws_sdk_opensearch.types.data_source_type.DataSourceType"
    ]
    """<p>The type of data source.</p>"""
    name: NotRequired["aws_sdk_opensearch.types.data_source_name.DataSourceName"]
    """<p>The name of the data source.</p>"""
    description: NotRequired[
        "aws_sdk_opensearch.types.data_source_description.DataSourceDescription"
    ]
    """<p>A description of the data source.</p>"""
    status: NotRequired["aws_sdk_opensearch.types.data_source_status.DataSourceStatus"]
    """<p>The status of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceResponse) -> dict:
    out: dict = {}
    if "data_source_type" in value:
        import aws_sdk_opensearch.types.data_source_type

        out["DataSourceType"] = (
            aws_sdk_opensearch.types.data_source_type.serialize_json(
                value["data_source_type"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_opensearch.types.data_source_status

        out["Status"] = aws_sdk_opensearch.types.data_source_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> GetDataSourceResponse:
    out: GetDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "DataSourceType" in data:
        import aws_sdk_opensearch.types.data_source_type

        out["data_source_type"] = (
            aws_sdk_opensearch.types.data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_opensearch.types.data_source_status

        out["status"] = aws_sdk_opensearch.types.data_source_status.deserialize_json(
            data["Status"]
        )
    return out
