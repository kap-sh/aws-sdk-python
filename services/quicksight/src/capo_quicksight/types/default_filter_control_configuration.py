"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultFilterControlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.control_title_format_text
    import capo_quicksight.types.default_filter_control_options
    import capo_quicksight.types.sheet_control_title


class DefaultFilterControlConfiguration(TypedDict, closed=True):
    title: "capo_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>DefaultFilterControlConfiguration</code>. This title is shared by all controls that are tied to this filter.</p>"""
    control_options: "capo_quicksight.types.default_filter_control_options.DefaultFilterControlOptions"
    """<p>The control option for the <code>DefaultFilterControlConfiguration</code>.</p>"""
    control_title_format_text: NotRequired[
        "capo_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the default filter control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultFilterControlConfiguration) -> dict:
    out: dict = {}
    out["Title"] = value.get("title", "")
    import capo_quicksight.types.default_filter_control_options

    out["ControlOptions"] = (
        capo_quicksight.types.default_filter_control_options.serialize_json(
            value["control_options"]
        )
    )
    if "control_title_format_text" in value:
        import capo_quicksight.types.control_title_format_text

        out["ControlTitleFormatText"] = (
            capo_quicksight.types.control_title_format_text.serialize_json(
                value["control_title_format_text"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultFilterControlConfiguration:
    out: DefaultFilterControlConfiguration = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if "ControlOptions" in data:
        import capo_quicksight.types.default_filter_control_options

        out["control_options"] = (
            capo_quicksight.types.default_filter_control_options.deserialize_json(
                data["ControlOptions"]
            )
        )
    else:
        raise DeserializationError(
            "DefaultFilterControlConfiguration.control_options required"
        )
    if "ControlTitleFormatText" in data:
        import capo_quicksight.types.control_title_format_text

        out["control_title_format_text"] = (
            capo_quicksight.types.control_title_format_text.deserialize_json(
                data["ControlTitleFormatText"]
            )
        )
    return out
