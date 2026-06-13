"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramVisual``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.histogram_configuration
    import aws_sdk_quicksight.types.long_plain_text
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.visual_custom_action_list
    import aws_sdk_quicksight.types.visual_subtitle_label_options
    import aws_sdk_quicksight.types.visual_title_label_options


class HistogramVisual(TypedDict):
    visual_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.</p>"""
    title: NotRequired[
        "aws_sdk_quicksight.types.visual_title_label_options.VisualTitleLabelOptions"
    ]
    """<p>The title that is displayed on the visual.</p>"""
    subtitle: NotRequired[
        "aws_sdk_quicksight.types.visual_subtitle_label_options.VisualSubtitleLabelOptions"
    ]
    """<p>The subtitle that is displayed on the visual.</p>"""
    chart_configuration: NotRequired[
        "aws_sdk_quicksight.types.histogram_configuration.HistogramConfiguration"
    ]
    """<p>The configuration for a <code>HistogramVisual</code>.</p>"""
    actions: NotRequired[
        "aws_sdk_quicksight.types.visual_custom_action_list.VisualCustomActionList"
    ]
    """<p>The list of custom actions that are configured for a visual.</p>"""
    visual_content_alt_text: NotRequired[
        "aws_sdk_quicksight.types.long_plain_text.LongPlainText"
    ]
    """<p>The alt text for the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistogramVisual) -> dict:
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
        import aws_sdk_quicksight.types.histogram_configuration

        out["ChartConfiguration"] = (
            aws_sdk_quicksight.types.histogram_configuration.serialize_json(
                value["chart_configuration"]
            )
        )
    if "actions" in value:
        import aws_sdk_quicksight.types.visual_custom_action_list

        out["Actions"] = (
            aws_sdk_quicksight.types.visual_custom_action_list.serialize_json(
                value["actions"]
            )
        )
    if "visual_content_alt_text" in value:
        out["VisualContentAltText"] = value["visual_content_alt_text"]
    return out


def deserialize_json(data: dict) -> HistogramVisual:
    out: HistogramVisual = {}  # type: ignore[typeddict-item]
    if "VisualId" in data:
        out["visual_id"] = data["VisualId"]
    else:
        raise DeserializationError("HistogramVisual.visual_id required")
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
        import aws_sdk_quicksight.types.histogram_configuration

        out["chart_configuration"] = (
            aws_sdk_quicksight.types.histogram_configuration.deserialize_json(
                data["ChartConfiguration"]
            )
        )
    if "Actions" in data:
        import aws_sdk_quicksight.types.visual_custom_action_list

        out["actions"] = (
            aws_sdk_quicksight.types.visual_custom_action_list.deserialize_json(
                data["Actions"]
            )
        )
    if "VisualContentAltText" in data:
        out["visual_content_alt_text"] = data["VisualContentAltText"]
    return out
