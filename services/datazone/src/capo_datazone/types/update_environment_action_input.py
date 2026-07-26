"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateEnvironmentActionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.action_parameters
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id


class UpdateEnvironmentActionInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The domain ID of the environment action.</p>"""
    environment_identifier: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The environment ID of the environment action.</p>"""
    identifier: "str"
    """<p>The ID of the environment action.</p>"""
    parameters: NotRequired["capo_datazone.types.action_parameters.ActionParameters"]
    """<p>The parameters of the environment action.</p>"""
    name: NotRequired["str"]
    """<p>The name of the environment action.</p>"""
    description: NotRequired["str"]
    """<p>The description of the environment action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentActionInput) -> dict:
    out: dict = {}
    if "parameters" in value:
        import capo_datazone.types.action_parameters

        out["parameters"] = capo_datazone.types.action_parameters.serialize_json(
            value["parameters"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentActionInput:
    out: UpdateEnvironmentActionInput = {}  # type: ignore[typeddict-item]
    if "parameters" in data:
        import capo_datazone.types.action_parameters

        out["parameters"] = capo_datazone.types.action_parameters.deserialize_json(
            data["parameters"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    return out
