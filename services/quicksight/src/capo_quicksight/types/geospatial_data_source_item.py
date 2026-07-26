"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialDataSourceItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_static_file_source


class GeospatialDataSourceItem(TypedDict, closed=True):
    static_file_data_source: NotRequired[
        "capo_quicksight.types.geospatial_static_file_source.GeospatialStaticFileSource"
    ]
    """<p>The static file data source properties for the geospatial data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialDataSourceItem) -> dict:
    out: dict = {}
    if "static_file_data_source" in value:
        import capo_quicksight.types.geospatial_static_file_source

        out["StaticFileDataSource"] = (
            capo_quicksight.types.geospatial_static_file_source.serialize_json(
                value["static_file_data_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialDataSourceItem:
    out: GeospatialDataSourceItem = {}  # type: ignore[typeddict-item]
    if "StaticFileDataSource" in data:
        import capo_quicksight.types.geospatial_static_file_source

        out["static_file_data_source"] = (
            capo_quicksight.types.geospatial_static_file_source.deserialize_json(
                data["StaticFileDataSource"]
            )
        )
    return out
