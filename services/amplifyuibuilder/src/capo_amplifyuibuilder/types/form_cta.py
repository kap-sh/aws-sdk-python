"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormCTA``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.form_button
    import capo_amplifyuibuilder.types.form_buttons_position


class FormCTA(TypedDict, closed=True):
    position: NotRequired[
        "capo_amplifyuibuilder.types.form_buttons_position.FormButtonsPosition"
    ]
    """<p>The position of the button.</p>"""
    clear: NotRequired["capo_amplifyuibuilder.types.form_button.FormButton"]
    """<p>Displays a clear button.</p>"""
    cancel: NotRequired["capo_amplifyuibuilder.types.form_button.FormButton"]
    """<p>Displays a cancel button.</p>"""
    submit: NotRequired["capo_amplifyuibuilder.types.form_button.FormButton"]
    """<p>Displays a submit button.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormCTA) -> dict:
    out: dict = {}
    if "position" in value:
        import capo_amplifyuibuilder.types.form_buttons_position

        out["position"] = (
            capo_amplifyuibuilder.types.form_buttons_position.serialize_json(
                value["position"]
            )
        )
    if "clear" in value:
        import capo_amplifyuibuilder.types.form_button

        out["clear"] = capo_amplifyuibuilder.types.form_button.serialize_json(
            value["clear"]
        )
    if "cancel" in value:
        import capo_amplifyuibuilder.types.form_button

        out["cancel"] = capo_amplifyuibuilder.types.form_button.serialize_json(
            value["cancel"]
        )
    if "submit" in value:
        import capo_amplifyuibuilder.types.form_button

        out["submit"] = capo_amplifyuibuilder.types.form_button.serialize_json(
            value["submit"]
        )
    return out


def deserialize_json(data: dict) -> FormCTA:
    out: FormCTA = {}  # type: ignore[typeddict-item]
    if "position" in data:
        import capo_amplifyuibuilder.types.form_buttons_position

        out["position"] = (
            capo_amplifyuibuilder.types.form_buttons_position.deserialize_json(
                data["position"]
            )
        )
    if "clear" in data:
        import capo_amplifyuibuilder.types.form_button

        out["clear"] = capo_amplifyuibuilder.types.form_button.deserialize_json(
            data["clear"]
        )
    if "cancel" in data:
        import capo_amplifyuibuilder.types.form_button

        out["cancel"] = capo_amplifyuibuilder.types.form_button.deserialize_json(
            data["cancel"]
        )
    if "submit" in data:
        import capo_amplifyuibuilder.types.form_button

        out["submit"] = capo_amplifyuibuilder.types.form_button.deserialize_json(
            data["submit"]
        )
    return out
