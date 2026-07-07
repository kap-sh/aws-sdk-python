"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filled_map_dimension_field_list
    import aws_sdk_quicksight.types.filled_map_measure_field_list


class FilledMapAggregatedFieldWells(TypedDict, closed=True):
    geospatial: NotRequired[
        "aws_sdk_quicksight.types.filled_map_dimension_field_list.FilledMapDimensionFieldList"
    ]
    """<p>The aggregated location field well of the filled map. Values are grouped by location fields.</p>"""
    values: NotRequired[
        "aws_sdk_quicksight.types.filled_map_measure_field_list.FilledMapMeasureFieldList"
    ]
    """<p>The aggregated color field well of a filled map. Values are aggregated based on location fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapAggregatedFieldWells) -> dict:
    out: dict = {}
    if "geospatial" in value:
        import aws_sdk_quicksight.types.filled_map_dimension_field_list

        out["Geospatial"] = (
            aws_sdk_quicksight.types.filled_map_dimension_field_list.serialize_json(
                value["geospatial"]
            )
        )
    if "values" in value:
        import aws_sdk_quicksight.types.filled_map_measure_field_list

        out["Values"] = (
            aws_sdk_quicksight.types.filled_map_measure_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilledMapAggregatedFieldWells:
    out: FilledMapAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Geospatial" in data:
        import aws_sdk_quicksight.types.filled_map_dimension_field_list

        out["geospatial"] = (
            aws_sdk_quicksight.types.filled_map_dimension_field_list.deserialize_json(
                data["Geospatial"]
            )
        )
    if "Values" in data:
        import aws_sdk_quicksight.types.filled_map_measure_field_list

        out["values"] = (
            aws_sdk_quicksight.types.filled_map_measure_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out
