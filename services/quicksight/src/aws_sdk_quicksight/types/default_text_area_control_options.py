"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultTextAreaControlOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.text_area_control_delimiter
    import aws_sdk_quicksight.types.text_area_control_display_options


class DefaultTextAreaControlOptions(TypedDict):
    delimiter: NotRequired[
        "aws_sdk_quicksight.types.text_area_control_delimiter.TextAreaControlDelimiter"
    ]
    """<p>The delimiter that is used to separate the lines in text.</p>"""
    display_options: NotRequired[
        "aws_sdk_quicksight.types.text_area_control_display_options.TextAreaControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultTextAreaControlOptions) -> dict:
    out: dict = {}
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    if "display_options" in value:
        import aws_sdk_quicksight.types.text_area_control_display_options

        out["DisplayOptions"] = (
            aws_sdk_quicksight.types.text_area_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultTextAreaControlOptions:
    out: DefaultTextAreaControlOptions = {}  # type: ignore[typeddict-item]
    if "Delimiter" in data:
        out["delimiter"] = data["Delimiter"]
    if "DisplayOptions" in data:
        import aws_sdk_quicksight.types.text_area_control_display_options

        out["display_options"] = (
            aws_sdk_quicksight.types.text_area_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    return out
