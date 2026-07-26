"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterSliderControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.control_title_format_text
    import capo_quicksight.types.double
    import capo_quicksight.types.sheet_control_slider_type
    import capo_quicksight.types.sheet_control_title
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.slider_control_display_options


class FilterSliderControl(TypedDict, closed=True):
    filter_control_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the <code>FilterSliderControl</code>.</p>"""
    title: "capo_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>FilterSliderControl</code>.</p>"""
    source_filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The source filter ID of the <code>FilterSliderControl</code>.</p>"""
    display_options: NotRequired[
        "capo_quicksight.types.slider_control_display_options.SliderControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    type: NotRequired[
        "capo_quicksight.types.sheet_control_slider_type.SheetControlSliderType"
    ]
    """<p>The type of the <code>FilterSliderControl</code>. Choose one of the following options:</p> <ul> <li> <p> <code>SINGLE_POINT</code>: Filter against(equals) a single data point.</p> </li> <li> <p> <code>RANGE</code>: Filter data that is in a specified range.</p> </li> </ul>"""
    maximum_value: "capo_quicksight.types.double.Double"
    """<p>The larger value that is displayed at the right of the slider.</p>"""
    minimum_value: "capo_quicksight.types.double.Double"
    """<p>The smaller value that is displayed at the left of the slider.</p>"""
    step_size: "capo_quicksight.types.double.Double"
    """<p>The number of increments that the slider bar is divided into.</p>"""
    control_title_format_text: NotRequired[
        "capo_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterSliderControl) -> dict:
    out: dict = {}
    out["FilterControlId"] = value["filter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceFilterId"] = value["source_filter_id"]
    if "display_options" in value:
        import capo_quicksight.types.slider_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.slider_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "type" in value:
        import capo_quicksight.types.sheet_control_slider_type

        out["Type"] = capo_quicksight.types.sheet_control_slider_type.serialize_json(
            value["type"]
        )
    out["MaximumValue"] = value.get("maximum_value", 0)
    out["MinimumValue"] = value.get("minimum_value", 0)
    out["StepSize"] = value.get("step_size", 0)
    if "control_title_format_text" in value:
        import capo_quicksight.types.control_title_format_text

        out["ControlTitleFormatText"] = (
            capo_quicksight.types.control_title_format_text.serialize_json(
                value["control_title_format_text"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterSliderControl:
    out: FilterSliderControl = {}  # type: ignore[typeddict-item]
    if "FilterControlId" in data:
        out["filter_control_id"] = data["FilterControlId"]
    else:
        raise DeserializationError("FilterSliderControl.filter_control_id required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if "SourceFilterId" in data:
        out["source_filter_id"] = data["SourceFilterId"]
    else:
        raise DeserializationError("FilterSliderControl.source_filter_id required")
    if "DisplayOptions" in data:
        import capo_quicksight.types.slider_control_display_options

        out["display_options"] = (
            capo_quicksight.types.slider_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if "Type" in data:
        import capo_quicksight.types.sheet_control_slider_type

        out["type"] = capo_quicksight.types.sheet_control_slider_type.deserialize_json(
            data["Type"]
        )
    if "MaximumValue" in data:
        out["maximum_value"] = data["MaximumValue"]
    else:
        out["maximum_value"] = 0
    if "MinimumValue" in data:
        out["minimum_value"] = data["MinimumValue"]
    else:
        out["minimum_value"] = 0
    if "StepSize" in data:
        out["step_size"] = data["StepSize"]
    else:
        out["step_size"] = 0
    if "ControlTitleFormatText" in data:
        import capo_quicksight.types.control_title_format_text

        out["control_title_format_text"] = (
            capo_quicksight.types.control_title_format_text.deserialize_json(
                data["ControlTitleFormatText"]
            )
        )
    return out
