"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentActionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.action_parameters
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_action_id
    import capo_datazone.types.environment_id


class CreateEnvironmentActionOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which the environment action is created.</p>"""
    environment_id: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the environment in which the environment is created.</p>"""
    id: "capo_datazone.types.environment_action_id.EnvironmentActionId"
    """<p>The ID of the environment action.</p>"""
    name: "str"
    """<p>The name of the environment action.</p>"""
    parameters: "capo_datazone.types.action_parameters.ActionParameters"
    """<p>The parameters of the environment action.</p>"""
    description: NotRequired["str"]
    """<p>The description of the environment action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentActionOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["environmentId"] = value["environment_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_datazone.types.action_parameters

    out["parameters"] = capo_datazone.types.action_parameters.serialize_json(
        value["parameters"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentActionOutput:
    out: CreateEnvironmentActionOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateEnvironmentActionOutput.domain_id required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "CreateEnvironmentActionOutput.environment_id required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateEnvironmentActionOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentActionOutput.name required")
    if "parameters" in data:
        import capo_datazone.types.action_parameters

        out["parameters"] = capo_datazone.types.action_parameters.deserialize_json(
            data["parameters"]
        )
    else:
        raise DeserializationError("CreateEnvironmentActionOutput.parameters required")
    if "description" in data:
        out["description"] = data["description"]
    return out
