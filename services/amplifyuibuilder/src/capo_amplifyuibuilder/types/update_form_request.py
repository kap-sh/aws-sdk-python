"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateFormRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.update_form_data
    import capo_amplifyuibuilder.types.uuid


class UpdateFormRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID for the Amplify app.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID for the form.</p>"""
    client_token: NotRequired["str"]
    """<p>The unique client token.</p>"""
    updated_form: "capo_amplifyuibuilder.types.update_form_data.UpdateFormData"
    """<p>The request accepts the following data in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFormRequest) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.update_form_data

    out["updatedForm"] = capo_amplifyuibuilder.types.update_form_data.serialize_json(
        value["updated_form"]
    )
    return out


def deserialize_json(data: dict) -> UpdateFormRequest:
    out: UpdateFormRequest = {}  # type: ignore[typeddict-item]
    if "updatedForm" in data:
        import capo_amplifyuibuilder.types.update_form_data

        out["updated_form"] = (
            capo_amplifyuibuilder.types.update_form_data.deserialize_json(
                data["updatedForm"]
            )
        )
    else:
        raise DeserializationError("UpdateFormRequest.updated_form required")
    return out
