"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filled_map_field_wells
    import aws_sdk_quicksight.types.filled_map_sort_configuration
    import aws_sdk_quicksight.types.geospatial_map_style_options
    import aws_sdk_quicksight.types.geospatial_window_options
    import aws_sdk_quicksight.types.legend_options
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.visual_interaction_options


class FilledMapConfiguration(TypedDict):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.filled_map_field_wells.FilledMapFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.filled_map_sort_configuration.FilledMapSortConfiguration"
    ]
    """<p>The sort configuration of a <code>FilledMapVisual</code>.</p>"""
    legend: NotRequired["aws_sdk_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    tooltip: NotRequired["aws_sdk_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip display setup of the visual.</p>"""
    window_options: NotRequired[
        "aws_sdk_quicksight.types.geospatial_window_options.GeospatialWindowOptions"
    ]
    """<p>The window options of the filled map visual.</p>"""
    map_style_options: NotRequired[
        "aws_sdk_quicksight.types.geospatial_map_style_options.GeospatialMapStyleOptions"
    ]
    """<p>The map style options of the filled map visual.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.filled_map_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.filled_map_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.filled_map_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.filled_map_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "legend" in value:
        import aws_sdk_quicksight.types.legend_options

        out["Legend"] = aws_sdk_quicksight.types.legend_options.serialize_json(
            value["legend"]
        )
    if "tooltip" in value:
        import aws_sdk_quicksight.types.tooltip_options

        out["Tooltip"] = aws_sdk_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "window_options" in value:
        import aws_sdk_quicksight.types.geospatial_window_options

        out["WindowOptions"] = (
            aws_sdk_quicksight.types.geospatial_window_options.serialize_json(
                value["window_options"]
            )
        )
    if "map_style_options" in value:
        import aws_sdk_quicksight.types.geospatial_map_style_options

        out["MapStyleOptions"] = (
            aws_sdk_quicksight.types.geospatial_map_style_options.serialize_json(
                value["map_style_options"]
            )
        )
    if "interactions" in value:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilledMapConfiguration:
    out: FilledMapConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.filled_map_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.filled_map_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.filled_map_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.filled_map_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "Legend" in data:
        import aws_sdk_quicksight.types.legend_options

        out["legend"] = aws_sdk_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
        )
    if "Tooltip" in data:
        import aws_sdk_quicksight.types.tooltip_options

        out["tooltip"] = aws_sdk_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if "WindowOptions" in data:
        import aws_sdk_quicksight.types.geospatial_window_options

        out["window_options"] = (
            aws_sdk_quicksight.types.geospatial_window_options.deserialize_json(
                data["WindowOptions"]
            )
        )
    if "MapStyleOptions" in data:
        import aws_sdk_quicksight.types.geospatial_map_style_options

        out["map_style_options"] = (
            aws_sdk_quicksight.types.geospatial_map_style_options.deserialize_json(
                data["MapStyleOptions"]
            )
        )
    if "Interactions" in data:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out
