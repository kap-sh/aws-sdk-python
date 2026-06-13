"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateOperatorAppIdpConfigOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.idp_auth_configuration


class UpdateOperatorAppIdpConfigOutput(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    idp: "aws_sdk_devops_agent.types.idp_auth_configuration.IdpAuthConfiguration"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOperatorAppIdpConfigOutput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import aws_sdk_devops_agent.types.idp_auth_configuration

    out["idp"] = aws_sdk_devops_agent.types.idp_auth_configuration.serialize_json(
        value["idp"]
    )
    return out


def deserialize_json(data: dict) -> UpdateOperatorAppIdpConfigOutput:
    out: UpdateOperatorAppIdpConfigOutput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError(
            "UpdateOperatorAppIdpConfigOutput.agent_space_id required"
        )
    if "idp" in data:
        import aws_sdk_devops_agent.types.idp_auth_configuration

        out["idp"] = aws_sdk_devops_agent.types.idp_auth_configuration.deserialize_json(
            data["idp"]
        )
    else:
        raise DeserializationError("UpdateOperatorAppIdpConfigOutput.idp required")
    return out
