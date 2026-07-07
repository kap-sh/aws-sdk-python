"""Generated from Smithy shape ``com.amazonaws.quicksight#DropDownControlDisplayOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.label_options
    import aws_sdk_quicksight.types.list_control_select_all_options
    import aws_sdk_quicksight.types.sheet_control_info_icon_label_options


class DropDownControlDisplayOptions(TypedDict, closed=True):
    select_all_options: NotRequired[
        "aws_sdk_quicksight.types.list_control_select_all_options.ListControlSelectAllOptions"
    ]
    """<p>The configuration of the <code>Select all</code> options in a dropdown control.</p>"""
    title_options: NotRequired["aws_sdk_quicksight.types.label_options.LabelOptions"]
    """<p>The options to configure the title visibility, name, and font size.</p>"""
    info_icon_label_options: NotRequired[
        "aws_sdk_quicksight.types.sheet_control_info_icon_label_options.SheetControlInfoIconLabelOptions"
    ]
    """<p>The configuration of info icon label options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DropDownControlDisplayOptions) -> dict:
    out: dict = {}
    if "select_all_options" in value:
        import aws_sdk_quicksight.types.list_control_select_all_options

        out["SelectAllOptions"] = (
            aws_sdk_quicksight.types.list_control_select_all_options.serialize_json(
                value["select_all_options"]
            )
        )
    if "title_options" in value:
        import aws_sdk_quicksight.types.label_options

        out["TitleOptions"] = aws_sdk_quicksight.types.label_options.serialize_json(
            value["title_options"]
        )
    if "info_icon_label_options" in value:
        import aws_sdk_quicksight.types.sheet_control_info_icon_label_options

        out["InfoIconLabelOptions"] = (
            aws_sdk_quicksight.types.sheet_control_info_icon_label_options.serialize_json(
                value["info_icon_label_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DropDownControlDisplayOptions:
    out: DropDownControlDisplayOptions = {}  # type: ignore[typeddict-item]
    if "SelectAllOptions" in data:
        import aws_sdk_quicksight.types.list_control_select_all_options

        out["select_all_options"] = (
            aws_sdk_quicksight.types.list_control_select_all_options.deserialize_json(
                data["SelectAllOptions"]
            )
        )
    if "TitleOptions" in data:
        import aws_sdk_quicksight.types.label_options

        out["title_options"] = aws_sdk_quicksight.types.label_options.deserialize_json(
            data["TitleOptions"]
        )
    if "InfoIconLabelOptions" in data:
        import aws_sdk_quicksight.types.sheet_control_info_icon_label_options

        out["info_icon_label_options"] = (
            aws_sdk_quicksight.types.sheet_control_info_icon_label_options.deserialize_json(
                data["InfoIconLabelOptions"]
            )
        )
    return out
