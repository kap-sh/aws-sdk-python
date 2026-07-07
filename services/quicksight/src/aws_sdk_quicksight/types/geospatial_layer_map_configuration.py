"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerMapConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_map_layer_list
    import aws_sdk_quicksight.types.geospatial_map_state
    import aws_sdk_quicksight.types.geospatial_map_style
    import aws_sdk_quicksight.types.legend_options
    import aws_sdk_quicksight.types.visual_interaction_options


class GeospatialLayerMapConfiguration(TypedDict, closed=True):
    legend: NotRequired["aws_sdk_quicksight.types.legend_options.LegendOptions"]
    map_layers: NotRequired[
        "aws_sdk_quicksight.types.geospatial_map_layer_list.GeospatialMapLayerList"
    ]
    """<p>The geospatial layers to visualize on the map.</p>"""
    map_state: NotRequired[
        "aws_sdk_quicksight.types.geospatial_map_state.GeospatialMapState"
    ]
    """<p>The map state properties for the map.</p>"""
    map_style: NotRequired[
        "aws_sdk_quicksight.types.geospatial_map_style.GeospatialMapStyle"
    ]
    """<p>The map style properties for the map.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLayerMapConfiguration) -> dict:
    out: dict = {}
    if "legend" in value:
        import aws_sdk_quicksight.types.legend_options

        out["Legend"] = aws_sdk_quicksight.types.legend_options.serialize_json(
            value["legend"]
        )
    if "map_layers" in value:
        import aws_sdk_quicksight.types.geospatial_map_layer_list

        out["MapLayers"] = (
            aws_sdk_quicksight.types.geospatial_map_layer_list.serialize_json(
                value["map_layers"]
            )
        )
    if "map_state" in value:
        import aws_sdk_quicksight.types.geospatial_map_state

        out["MapState"] = aws_sdk_quicksight.types.geospatial_map_state.serialize_json(
            value["map_state"]
        )
    if "map_style" in value:
        import aws_sdk_quicksight.types.geospatial_map_style

        out["MapStyle"] = aws_sdk_quicksight.types.geospatial_map_style.serialize_json(
            value["map_style"]
        )
    if "interactions" in value:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialLayerMapConfiguration:
    out: GeospatialLayerMapConfiguration = {}  # type: ignore[typeddict-item]
    if "Legend" in data:
        import aws_sdk_quicksight.types.legend_options

        out["legend"] = aws_sdk_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
        )
    if "MapLayers" in data:
        import aws_sdk_quicksight.types.geospatial_map_layer_list

        out["map_layers"] = (
            aws_sdk_quicksight.types.geospatial_map_layer_list.deserialize_json(
                data["MapLayers"]
            )
        )
    if "MapState" in data:
        import aws_sdk_quicksight.types.geospatial_map_state

        out["map_state"] = (
            aws_sdk_quicksight.types.geospatial_map_state.deserialize_json(
                data["MapState"]
            )
        )
    if "MapStyle" in data:
        import aws_sdk_quicksight.types.geospatial_map_style

        out["map_style"] = (
            aws_sdk_quicksight.types.geospatial_map_style.deserialize_json(
                data["MapStyle"]
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
