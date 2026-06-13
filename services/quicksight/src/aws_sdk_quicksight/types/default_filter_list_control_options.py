"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultFilterListControlOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.control_sort_configuration_list
    import aws_sdk_quicksight.types.filter_selectable_values
    import aws_sdk_quicksight.types.list_control_display_options
    import aws_sdk_quicksight.types.sheet_control_list_type


class DefaultFilterListControlOptions(TypedDict):
    display_options: NotRequired[
        "aws_sdk_quicksight.types.list_control_display_options.ListControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    type: NotRequired[
        "aws_sdk_quicksight.types.sheet_control_list_type.SheetControlListType"
    ]
    """<p>The type of the <code>DefaultFilterListControlOptions</code>. Choose one of the following options:</p> <ul> <li> <p> <code>MULTI_SELECT</code>: The user can select multiple entries from the list.</p> </li> <li> <p> <code>SINGLE_SELECT</code>: The user can select a single entry from the list.</p> </li> </ul>"""
    selectable_values: NotRequired[
        "aws_sdk_quicksight.types.filter_selectable_values.FilterSelectableValues"
    ]
    """<p>A list of selectable values that are used in a control.</p>"""
    control_sort_configurations: NotRequired[
        "aws_sdk_quicksight.types.control_sort_configuration_list.ControlSortConfigurationList"
    ]
    """<p>The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultFilterListControlOptions) -> dict:
    out: dict = {}
    if "display_options" in value:
        import aws_sdk_quicksight.types.list_control_display_options

        out["DisplayOptions"] = (
            aws_sdk_quicksight.types.list_control_display_options.serialize_json(
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
    if "control_sort_configurations" in value:
        import aws_sdk_quicksight.types.control_sort_configuration_list

        out["ControlSortConfigurations"] = (
            aws_sdk_quicksight.types.control_sort_configuration_list.serialize_json(
                value["control_sort_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultFilterListControlOptions:
    out: DefaultFilterListControlOptions = {}  # type: ignore[typeddict-item]
    if "DisplayOptions" in data:
        import aws_sdk_quicksight.types.list_control_display_options

        out["display_options"] = (
            aws_sdk_quicksight.types.list_control_display_options.deserialize_json(
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
    if "ControlSortConfigurations" in data:
        import aws_sdk_quicksight.types.control_sort_configuration_list

        out["control_sort_configurations"] = (
            aws_sdk_quicksight.types.control_sort_configuration_list.deserialize_json(
                data["ControlSortConfigurations"]
            )
        )
    return out
