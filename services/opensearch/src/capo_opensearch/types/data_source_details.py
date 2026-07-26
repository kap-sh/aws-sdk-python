"""Generated from Smithy shape ``com.amazonaws.opensearch#DataSourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.data_source_description
    import capo_opensearch.types.data_source_name
    import capo_opensearch.types.data_source_status
    import capo_opensearch.types.data_source_type


class DataSourceDetails(TypedDict, closed=True):
    data_source_type: NotRequired[
        "capo_opensearch.types.data_source_type.DataSourceType"
    ]
    """<p>The type of data source.</p>"""
    name: NotRequired["capo_opensearch.types.data_source_name.DataSourceName"]
    """<p>The name of the data source.</p>"""
    description: NotRequired[
        "capo_opensearch.types.data_source_description.DataSourceDescription"
    ]
    """<p>A description of the data source.</p>"""
    status: NotRequired["capo_opensearch.types.data_source_status.DataSourceStatus"]
    """<p>The status of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceDetails) -> dict:
    out: dict = {}
    if "data_source_type" in value:
        import capo_opensearch.types.data_source_type

        out["DataSourceType"] = capo_opensearch.types.data_source_type.serialize_json(
            value["data_source_type"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_opensearch.types.data_source_status

        out["Status"] = capo_opensearch.types.data_source_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> DataSourceDetails:
    out: DataSourceDetails = {}  # type: ignore[typeddict-item]
    if "DataSourceType" in data:
        import capo_opensearch.types.data_source_type

        out["data_source_type"] = (
            capo_opensearch.types.data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import capo_opensearch.types.data_source_status

        out["status"] = capo_opensearch.types.data_source_status.deserialize_json(
            data["Status"]
        )
    return out
