"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultFilterDropDownControlOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.commit_mode
    import aws_sdk_quicksight.types.control_sort_configuration_list
    import aws_sdk_quicksight.types.drop_down_control_display_options
    import aws_sdk_quicksight.types.filter_selectable_values
    import aws_sdk_quicksight.types.sheet_control_list_type


class DefaultFilterDropDownControlOptions(TypedDict, closed=True):
    display_options: NotRequired[
        "aws_sdk_quicksight.types.drop_down_control_display_options.DropDownControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    type: NotRequired[
        "aws_sdk_quicksight.types.sheet_control_list_type.SheetControlListType"
    ]
    """<p>The type of the <code>FilterDropDownControl</code>. Choose one of the following options:</p> <ul> <li> <p> <code>MULTI_SELECT</code>: The user can select multiple entries from a dropdown menu.</p> </li> <li> <p> <code>SINGLE_SELECT</code>: The user can select a single entry from a dropdown menu.</p> </li> </ul>"""
    selectable_values: NotRequired[
        "aws_sdk_quicksight.types.filter_selectable_values.FilterSelectableValues"
    ]
    """<p>A list of selectable values that are used in a control.</p>"""
    commit_mode: NotRequired["aws_sdk_quicksight.types.commit_mode.CommitMode"]
    """<p>The visibility configuration of the Apply button on a <code>FilterDropDownControl</code>.</p>"""
    control_sort_configurations: NotRequired[
        "aws_sdk_quicksight.types.control_sort_configuration_list.ControlSortConfigurationList"
    ]
    """<p>The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultFilterDropDownControlOptions) -> dict:
    out: dict = {}
    if "display_options" in value:
        import aws_sdk_quicksight.types.drop_down_control_display_options

        out["DisplayOptions"] = (
            aws_sdk_quicksight.types.drop_down_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "type" in value:
        import aws_sdk_quicksight.types.sheet_control_list_type

        out["Type"] = aws_sdk_quicksight.types.sheet_control_list_type.serialize_json(
            value["type"]
        )
    if "selectable_values" in value:
        import aws_sdk_quicksight.types.filter_selectable_values

        out["SelectableValues"] = (
            aws_sdk_quicksight.types.filter_selectable_values.serialize_json(
                value["selectable_values"]
            )
        )
    if "commit_mode" in value:
        import aws_sdk_quicksight.types.commit_mode

        out["CommitMode"] = aws_sdk_quicksight.types.commit_mode.serialize_json(
            value["commit_mode"]
        )
    if "control_sort_configurations" in value:
        import aws_sdk_quicksight.types.control_sort_configuration_list

        out["ControlSortConfigurations"] = (
            aws_sdk_quicksight.types.control_sort_configuration_list.serialize_json(
                value["control_sort_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultFilterDropDownControlOptions:
    out: DefaultFilterDropDownControlOptions = {}  # type: ignore[typeddict-item]
    if "DisplayOptions" in data:
        import aws_sdk_quicksight.types.drop_down_control_display_options

        out["display_options"] = (
            aws_sdk_quicksight.types.drop_down_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if "Type" in data:
        import aws_sdk_quicksight.types.sheet_control_list_type

        out["type"] = aws_sdk_quicksight.types.sheet_control_list_type.deserialize_json(
            data["Type"]
        )
    if "SelectableValues" in data:
        import aws_sdk_quicksight.types.filter_selectable_values

        out["selectable_values"] = (
            aws_sdk_quicksight.types.filter_selectable_values.deserialize_json(
                data["SelectableValues"]
            )
        )
    if "CommitMode" in data:
        import aws_sdk_quicksight.types.commit_mode

        out["commit_mode"] = aws_sdk_quicksight.types.commit_mode.deserialize_json(
            data["CommitMode"]
        )
    if "ControlSortConfigurations" in data:
        import aws_sdk_quicksight.types.control_sort_configuration_list

        out["control_sort_configurations"] = (
            aws_sdk_quicksight.types.control_sort_configuration_list.deserialize_json(
                data["ControlSortConfigurations"]
            )
        )
    return out
