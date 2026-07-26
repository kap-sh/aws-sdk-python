"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CreateComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.create_component_data


class CreateComponentRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app to associate with the component.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    client_token: NotRequired["str"]
    """<p>The unique client token.</p>"""
    component_to_create: (
        "capo_amplifyuibuilder.types.create_component_data.CreateComponentData"
    )
    """<p>Represents the configuration of the component to create.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComponentRequest) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.create_component_data

    out["componentToCreate"] = (
        capo_amplifyuibuilder.types.create_component_data.serialize_json(
            value["component_to_create"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateComponentRequest:
    out: CreateComponentRequest = {}  # type: ignore[typeddict-item]
    if "componentToCreate" in data:
        import capo_amplifyuibuilder.types.create_component_data

        out["component_to_create"] = (
            capo_amplifyuibuilder.types.create_component_data.deserialize_json(
                data["componentToCreate"]
            )
        )
    else:
        raise DeserializationError(
            "CreateComponentRequest.component_to_create required"
        )
    return out
