"""Generated from Smithy shape ``com.amazonaws.quicksight#TextFieldControlDisplayOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.label_options
    import aws_sdk_quicksight.types.sheet_control_info_icon_label_options
    import aws_sdk_quicksight.types.text_control_placeholder_options


class TextFieldControlDisplayOptions(TypedDict):
    title_options: NotRequired["aws_sdk_quicksight.types.label_options.LabelOptions"]
    """<p>The options to configure the title visibility, name, and font size.</p>"""
    placeholder_options: NotRequired[
        "aws_sdk_quicksight.types.text_control_placeholder_options.TextControlPlaceholderOptions"
    ]
    """<p>The configuration of the placeholder options in a text field control.</p>"""
    info_icon_label_options: NotRequired[
        "aws_sdk_quicksight.types.sheet_control_info_icon_label_options.SheetControlInfoIconLabelOptions"
    ]
    """<p>The configuration of info icon label options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextFieldControlDisplayOptions) -> dict:
    out: dict = {}
    if "title_options" in value:
        import aws_sdk_quicksight.types.label_options

        out["TitleOptions"] = aws_sdk_quicksight.types.label_options.serialize_json(
            value["title_options"]
        )
    if "placeholder_options" in value:
        import aws_sdk_quicksight.types.text_control_placeholder_options

        out["PlaceholderOptions"] = (
            aws_sdk_quicksight.types.text_control_placeholder_options.serialize_json(
                value["placeholder_options"]
            )
        )
    if "info_icon_label_options" in value:
        import aws_sdk_quicksight.types.sheet_control_info_icon_label_options

        out["InfoIconLabelOptions"] = (
            aws_sdk_quicksight.types.sheet_control_info_icon_label_options.serialize_json(
                value["info_icon_label_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextFieldControlDisplayOptions:
    out: TextFieldControlDisplayOptions = {}  # type: ignore[typeddict-item]
    if "TitleOptions" in data:
        import aws_sdk_quicksight.types.label_options

        out["title_options"] = aws_sdk_quicksight.types.label_options.deserialize_json(
            data["TitleOptions"]
        )
    if "PlaceholderOptions" in data:
        import aws_sdk_quicksight.types.text_control_placeholder_options

        out["placeholder_options"] = (
            aws_sdk_quicksight.types.text_control_placeholder_options.deserialize_json(
                data["PlaceholderOptions"]
            )
        )
    if "InfoIconLabelOptions" in data:
        import aws_sdk_quicksight.types.sheet_control_info_icon_label_options

        out["info_icon_label_options"] = (
            aws_sdk_quicksight.types.sheet_control_info_icon_label_options.deserialize_json(
                data["InfoIconLabelOptions"]
            )
        )
    return out
