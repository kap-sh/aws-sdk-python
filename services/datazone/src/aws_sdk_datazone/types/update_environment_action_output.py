"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateEnvironmentActionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.action_parameters
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_action_id
    import aws_sdk_datazone.types.environment_id


class UpdateEnvironmentActionOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The domain ID of the environment action.</p>"""
    environment_id: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The environment ID of the environment action.</p>"""
    id: "aws_sdk_datazone.types.environment_action_id.EnvironmentActionId"
    """<p>The ID of the environment action.</p>"""
    name: "str"
    """<p>The name of the environment action.</p>"""
    parameters: "aws_sdk_datazone.types.action_parameters.ActionParameters"
    """<p>The parameters of the environment action.</p>"""
    description: NotRequired["str"]
    """<p>The description of the environment action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentActionOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["environmentId"] = value["environment_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import aws_sdk_datazone.types.action_parameters

    out["parameters"] = aws_sdk_datazone.types.action_parameters.serialize_json(
        value["parameters"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentActionOutput:
    out: UpdateEnvironmentActionOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("UpdateEnvironmentActionOutput.domain_id required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "UpdateEnvironmentActionOutput.environment_id required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateEnvironmentActionOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateEnvironmentActionOutput.name required")
    if "parameters" in data:
        import aws_sdk_datazone.types.action_parameters

        out["parameters"] = aws_sdk_datazone.types.action_parameters.deserialize_json(
            data["parameters"]
        )
    else:
        raise DeserializationError("UpdateEnvironmentActionOutput.parameters required")
    if "description" in data:
        out["description"] = data["description"]
    return out
