"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentActionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.action_parameters
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id


class CreateEnvironmentActionInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the environment action is created.</p>"""
    environment_identifier: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the environment in which the environment action is created.</p>"""
    name: "str"
    """<p>The name of the environment action.</p>"""
    parameters: "capo_datazone.types.action_parameters.ActionParameters"
    """<p>The parameters of the environment action.</p>"""
    description: NotRequired["str"]
    """<p>The description of the environment action that is being created in the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentActionInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_datazone.types.action_parameters

    out["parameters"] = capo_datazone.types.action_parameters.serialize_json(
        value["parameters"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentActionInput:
    out: CreateEnvironmentActionInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentActionInput.name required")
    if "parameters" in data:
        import capo_datazone.types.action_parameters

        out["parameters"] = capo_datazone.types.action_parameters.deserialize_json(
            data["parameters"]
        )
    else:
        raise DeserializationError("CreateEnvironmentActionInput.parameters required")
    if "description" in data:
        out["description"] = data["description"]
    return out
