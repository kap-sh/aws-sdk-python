"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisual``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.long_plain_text
    import aws_sdk_quicksight.types.plugin_visual_configuration
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.visual_custom_action_list
    import aws_sdk_quicksight.types.visual_subtitle_label_options
    import aws_sdk_quicksight.types.visual_title_label_options


class PluginVisual(TypedDict):
    visual_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the visual that you want to use.</p>"""
    plugin_arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that reflects the plugin and version.</p>"""
    title: NotRequired[
        "aws_sdk_quicksight.types.visual_title_label_options.VisualTitleLabelOptions"
    ]
    subtitle: NotRequired[
        "aws_sdk_quicksight.types.visual_subtitle_label_options.VisualSubtitleLabelOptions"
    ]
    chart_configuration: NotRequired[
        "aws_sdk_quicksight.types.plugin_visual_configuration.PluginVisualConfiguration"
    ]
    """<p> A description of the plugin field wells and their persisted properties. </p>"""
    actions: NotRequired[
        "aws_sdk_quicksight.types.visual_custom_action_list.VisualCustomActionList"
    ]
    """<p>The list of custom actions that are configured for a visual.</p>"""
    visual_content_alt_text: NotRequired[
        "aws_sdk_quicksight.types.long_plain_text.LongPlainText"
    ]
    """<p>The alt text for the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisual) -> dict:
    out: dict = {}
    out["VisualId"] = value["visual_id"]
    out["PluginArn"] = value["plugin_arn"]
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
        import aws_sdk_quicksight.types.plugin_visual_configuration

        out["ChartConfiguration"] = (
            aws_sdk_quicksight.types.plugin_visual_configuration.serialize_json(
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


def deserialize_json(data: dict) -> PluginVisual:
    out: PluginVisual = {}  # type: ignore[typeddict-item]
    if "VisualId" in data:
        out["visual_id"] = data["VisualId"]
    else:
        raise DeserializationError("PluginVisual.visual_id required")
    if "PluginArn" in data:
        out["plugin_arn"] = data["PluginArn"]
    else:
        raise DeserializationError("PluginVisual.plugin_arn required")
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
        import aws_sdk_quicksight.types.plugin_visual_configuration

        out["chart_configuration"] = (
            aws_sdk_quicksight.types.plugin_visual_configuration.deserialize_json(
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
