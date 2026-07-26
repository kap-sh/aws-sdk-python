"""Generated from Smithy shape ``com.amazonaws.medialive#CreateNodeRegistrationScriptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class CreateNodeRegistrationScriptResponse(TypedDict, closed=True):
    node_registration_script: NotRequired["capo_medialive.types.__string.__string"]
    """A script that can be run on a Bring Your Own Device Elemental Anywhere system to create a node in a cluster."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodeRegistrationScriptResponse) -> dict:
    out: dict = {}
    if "node_registration_script" in value:
        out["nodeRegistrationScript"] = value["node_registration_script"]
    return out


def deserialize_json(data: dict) -> CreateNodeRegistrationScriptResponse:
    out: CreateNodeRegistrationScriptResponse = {}  # type: ignore[typeddict-item]
    if "nodeRegistrationScript" in data:
        out["node_registration_script"] = data["nodeRegistrationScript"]
    return out
