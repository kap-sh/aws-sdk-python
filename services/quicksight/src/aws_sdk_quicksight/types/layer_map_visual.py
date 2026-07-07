"""Generated from Smithy shape ``com.amazonaws.quicksight#LayerMapVisual``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_identifier
    import aws_sdk_quicksight.types.geospatial_layer_map_configuration
    import aws_sdk_quicksight.types.long_plain_text
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.visual_subtitle_label_options
    import aws_sdk_quicksight.types.visual_title_label_options


class LayerMapVisual(TypedDict, closed=True):
    visual_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the visual.</p>"""
    title: NotRequired[
        "aws_sdk_quicksight.types.visual_title_label_options.VisualTitleLabelOptions"
    ]
    subtitle: NotRequired[
        "aws_sdk_quicksight.types.visual_subtitle_label_options.VisualSubtitleLabelOptions"
    ]
    chart_configuration: NotRequired[
        "aws_sdk_quicksight.types.geospatial_layer_map_configuration.GeospatialLayerMapConfiguration"
    ]
    """<p>The configuration settings of the visual.</p>"""
    data_set_identifier: (
        "aws_sdk_quicksight.types.data_set_identifier.DataSetIdentifier"
    )
    """<p>The dataset that is used to create the layer map visual. You can't create a visual without a dataset.</p>"""
    visual_content_alt_text: NotRequired[
        "aws_sdk_quicksight.types.long_plain_text.LongPlainText"
    ]
    """<p>The alt text for the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayerMapVisual) -> dict:
    out: dict = {}
    out["VisualId"] = value["visual_id"]
    if "title" in value:
        import aws_sdk_quicksight.types.visual_title_label_options

        out["Title"] = (
            aws_sdk_quicksight.types.visual_title_label_options.serialize_json(
                value["title"]
            )
        )
    if "subtitle" in value:
        import aws_sdk_quicksight.types.visual_subtitle_label_options

        out["Subtitle"] = (
            aws_sdk_quicksight.types.visual_subtitle_label_options.serialize_json(
                value["subtitle"]
            )
        )
    if "chart_configuration" in value:
        import aws_sdk_quicksight.types.geospatial_layer_map_configuration

        out["ChartConfiguration"] = (
            aws_sdk_quicksight.types.geospatial_layer_map_configuration.serialize_json(
                value["chart_configuration"]
            )
        )
    out["DataSetIdentifier"] = value["data_set_identifier"]
    if "visual_content_alt_text" in value:
        out["VisualContentAltText"] = value["visual_content_alt_text"]
    return out


def deserialize_json(data: dict) -> LayerMapVisual:
    out: LayerMapVisual = {}  # type: ignore[typeddict-item]
    if "VisualId" in data:
        out["visual_id"] = data["VisualId"]
    else:
        raise DeserializationError("LayerMapVisual.visual_id required")
    if "Title" in data:
        import aws_sdk_quicksight.types.visual_title_label_options

        out["title"] = (
            aws_sdk_quicksight.types.visual_title_label_options.deserialize_json(
                data["Title"]
            )
        )
    if "Subtitle" in data:
        import aws_sdk_quicksight.types.visual_subtitle_label_options

        out["subtitle"] = (
            aws_sdk_quicksight.types.visual_subtitle_label_options.deserialize_json(
                data["Subtitle"]
            )
        )
    if "ChartConfiguration" in data:
        import aws_sdk_quicksight.types.geospatial_layer_map_configuration

        out["chart_configuration"] = (
            aws_sdk_quicksight.types.geospatial_layer_map_configuration.deserialize_json(
                data["ChartConfiguration"]
            )
        )
    if "DataSetIdentifier" in data:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    else:
        raise DeserializationError("LayerMapVisual.data_set_identifier required")
    if "VisualContentAltText" in data:
        out["visual_content_alt_text"] = data["VisualContentAltText"]
    return out
