"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormCTA``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.form_button
    import aws_sdk_amplifyuibuilder.types.form_buttons_position


class FormCTA(TypedDict):
    position: NotRequired[
        "aws_sdk_amplifyuibuilder.types.form_buttons_position.FormButtonsPosition"
    ]
    """<p>The position of the button.</p>"""
    clear: NotRequired["aws_sdk_amplifyuibuilder.types.form_button.FormButton"]
    """<p>Displays a clear button.</p>"""
    cancel: NotRequired["aws_sdk_amplifyuibuilder.types.form_button.FormButton"]
    """<p>Displays a cancel button.</p>"""
    submit: NotRequired["aws_sdk_amplifyuibuilder.types.form_button.FormButton"]
    """<p>Displays a submit button.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormCTA) -> dict:
    out: dict = {}
    if "position" in value:
        import aws_sdk_amplifyuibuilder.types.form_buttons_position

        out["position"] = (
            aws_sdk_amplifyuibuilder.types.form_buttons_position.serialize_json(
                value["position"]
            )
        )
    if "clear" in value:
        import aws_sdk_amplifyuibuilder.types.form_button

        out["clear"] = aws_sdk_amplifyuibuilder.types.form_button.serialize_json(
            value["clear"]
        )
    if "cancel" in value:
        import aws_sdk_amplifyuibuilder.types.form_button

        out["cancel"] = aws_sdk_amplifyuibuilder.types.form_button.serialize_json(
            value["cancel"]
        )
    if "submit" in value:
        import aws_sdk_amplifyuibuilder.types.form_button

        out["submit"] = aws_sdk_amplifyuibuilder.types.form_button.serialize_json(
            value["submit"]
        )
    return out


def deserialize_json(data: dict) -> FormCTA:
    out: FormCTA = {}  # type: ignore[typeddict-item]
    if "position" in data:
        import aws_sdk_amplifyuibuilder.types.form_buttons_position

        out["position"] = (
            aws_sdk_amplifyuibuilder.types.form_buttons_position.deserialize_json(
                data["position"]
            )
        )
    if "clear" in data:
        import aws_sdk_amplifyuibuilder.types.form_button

        out["clear"] = aws_sdk_amplifyuibuilder.types.form_button.deserialize_json(
            data["clear"]
        )
    if "cancel" in data:
        import aws_sdk_amplifyuibuilder.types.form_button

        out["cancel"] = aws_sdk_amplifyuibuilder.types.form_button.deserialize_json(
            data["cancel"]
        )
    if "submit" in data:
        import aws_sdk_amplifyuibuilder.types.form_button

        out["submit"] = aws_sdk_amplifyuibuilder.types.form_button.deserialize_json(
            data["submit"]
        )
    return out
