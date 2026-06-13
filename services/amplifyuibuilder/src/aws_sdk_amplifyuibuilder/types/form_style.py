"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormStyle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.form_style_config


class FormStyle(TypedDict):
    horizontal_gap: NotRequired[
        "aws_sdk_amplifyuibuilder.types.form_style_config.FormStyleConfig"
    ]
    """<p>The spacing for the horizontal gap.</p>"""
    vertical_gap: NotRequired[
        "aws_sdk_amplifyuibuilder.types.form_style_config.FormStyleConfig"
    ]
    """<p>The spacing for the vertical gap.</p>"""
    outer_padding: NotRequired[
        "aws_sdk_amplifyuibuilder.types.form_style_config.FormStyleConfig"
    ]
    """<p>The size of the outer padding for the form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormStyle) -> dict:
    out: dict = {}
    if "horizontal_gap" in value:
        import aws_sdk_amplifyuibuilder.types.form_style_config

        out["horizontalGap"] = (
            aws_sdk_amplifyuibuilder.types.form_style_config.serialize_json(
                value["horizontal_gap"]
            )
        )
    if "vertical_gap" in value:
        import aws_sdk_amplifyuibuilder.types.form_style_config

        out["verticalGap"] = (
            aws_sdk_amplifyuibuilder.types.form_style_config.serialize_json(
                value["vertical_gap"]
            )
        )
    if "outer_padding" in value:
        import aws_sdk_amplifyuibuilder.types.form_style_config

        out["outerPadding"] = (
            aws_sdk_amplifyuibuilder.types.form_style_config.serialize_json(
                value["outer_padding"]
            )
        )
    return out


def deserialize_json(data: dict) -> FormStyle:
    out: FormStyle = {}  # type: ignore[typeddict-item]
    if "horizontalGap" in data:
        import aws_sdk_amplifyuibuilder.types.form_style_config

        out["horizontal_gap"] = (
            aws_sdk_amplifyuibuilder.types.form_style_config.deserialize_json(
                data["horizontalGap"]
            )
        )
    if "verticalGap" in data:
        import aws_sdk_amplifyuibuilder.types.form_style_config

        out["vertical_gap"] = (
            aws_sdk_amplifyuibuilder.types.form_style_config.deserialize_json(
                data["verticalGap"]
            )
        )
    if "outerPadding" in data:
        import aws_sdk_amplifyuibuilder.types.form_style_config

        out["outer_padding"] = (
            aws_sdk_amplifyuibuilder.types.form_style_config.deserialize_json(
                data["outerPadding"]
            )
        )
    return out
