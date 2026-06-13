"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultTextFieldControlOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.text_field_control_display_options


class DefaultTextFieldControlOptions(TypedDict):
    display_options: NotRequired[
        "aws_sdk_quicksight.types.text_field_control_display_options.TextFieldControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultTextFieldControlOptions) -> dict:
    out: dict = {}
    if "display_options" in value:
        import aws_sdk_quicksight.types.text_field_control_display_options

        out["DisplayOptions"] = (
            aws_sdk_quicksight.types.text_field_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultTextFieldControlOptions:
    out: DefaultTextFieldControlOptions = {}  # type: ignore[typeddict-item]
    if "DisplayOptions" in data:
        import aws_sdk_quicksight.types.text_field_control_display_options

        out["display_options"] = (
            aws_sdk_quicksight.types.text_field_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    return out
