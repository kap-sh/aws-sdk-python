"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAssociationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.association_id
    import aws_sdk_devops_agent.types.service_configuration


class UpdateAssociationInput(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    association_id: "aws_sdk_devops_agent.types.association_id.AssociationId"
    """<p>The unique identifier of the given association.</p>"""
    configuration: (
        "aws_sdk_devops_agent.types.service_configuration.ServiceConfiguration"
    )
    """<p>The configuration that directs how AgentSpace interacts with the given service. The entire configuration is replaced on update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssociationInput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.service_configuration

    out["configuration"] = (
        aws_sdk_devops_agent.types.service_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAssociationInput:
    out: UpdateAssociationInput = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_devops_agent.types.service_configuration

        out["configuration"] = (
            aws_sdk_devops_agent.types.service_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("UpdateAssociationInput.configuration required")
    return out
