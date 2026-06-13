"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialDataSourceItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_static_file_source


class GeospatialDataSourceItem(TypedDict):
    static_file_data_source: NotRequired[
        "aws_sdk_quicksight.types.geospatial_static_file_source.GeospatialStaticFileSource"
    ]
    """<p>The static file data source properties for the geospatial data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialDataSourceItem) -> dict:
    out: dict = {}
    if "static_file_data_source" in value:
        import aws_sdk_quicksight.types.geospatial_static_file_source

        out["StaticFileDataSource"] = (
            aws_sdk_quicksight.types.geospatial_static_file_source.serialize_json(
                value["static_file_data_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialDataSourceItem:
    out: GeospatialDataSourceItem = {}  # type: ignore[typeddict-item]
    if "StaticFileDataSource" in data:
        import aws_sdk_quicksight.types.geospatial_static_file_source

        out["static_file_data_source"] = (
            aws_sdk_quicksight.types.geospatial_static_file_source.deserialize_json(
                data["StaticFileDataSource"]
            )
        )
    return out
