"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultDateTimePickerControlOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.commit_mode
    import capo_quicksight.types.date_time_picker_control_display_options
    import capo_quicksight.types.sheet_control_date_time_picker_type


class DefaultDateTimePickerControlOptions(TypedDict, closed=True):
    type: NotRequired[
        "capo_quicksight.types.sheet_control_date_time_picker_type.SheetControlDateTimePickerType"
    ]
    """<p>The date time picker type of the <code>DefaultDateTimePickerControlOptions</code>. Choose one of the following options:</p> <ul> <li> <p> <code>SINGLE_VALUED</code>: The filter condition is a fixed date.</p> </li> <li> <p> <code>DATE_RANGE</code>: The filter condition is a date time range.</p> </li> </ul>"""
    display_options: NotRequired[
        "capo_quicksight.types.date_time_picker_control_display_options.DateTimePickerControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    commit_mode: NotRequired["capo_quicksight.types.commit_mode.CommitMode"]
    """<p>The visibility configuration of the Apply button on a <code>DateTimePickerControl</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultDateTimePickerControlOptions) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_quicksight.types.sheet_control_date_time_picker_type

        out["Type"] = (
            capo_quicksight.types.sheet_control_date_time_picker_type.serialize_json(
                value["type"]
            )
        )
    if "display_options" in value:
        import capo_quicksight.types.date_time_picker_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.date_time_picker_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "commit_mode" in value:
        import capo_quicksight.types.commit_mode

        out["CommitMode"] = capo_quicksight.types.commit_mode.serialize_json(
            value["commit_mode"]
        )
    return out


def deserialize_json(data: dict) -> DefaultDateTimePickerControlOptions:
    out: DefaultDateTimePickerControlOptions = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_quicksight.types.sheet_control_date_time_picker_type

        out["type"] = (
            capo_quicksight.types.sheet_control_date_time_picker_type.deserialize_json(
                data["Type"]
            )
        )
    if "DisplayOptions" in data:
        import capo_quicksight.types.date_time_picker_control_display_options

        out["display_options"] = (
            capo_quicksight.types.date_time_picker_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if "CommitMode" in data:
        import capo_quicksight.types.commit_mode

        out["commit_mode"] = capo_quicksight.types.commit_mode.deserialize_json(
            data["CommitMode"]
        )
    return out
