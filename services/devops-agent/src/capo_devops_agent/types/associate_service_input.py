"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssociateServiceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.service_configuration
    import capo_devops_agent.types.service_id


class AssociateServiceInput(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    service_id: "capo_devops_agent.types.service_id.ServiceId"
    """<p>The unique identifier of the service.</p>"""
    configuration: "capo_devops_agent.types.service_configuration.ServiceConfiguration"
    """<p>The configuration that directs how AgentSpace interacts with the given service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateServiceInput) -> dict:
    out: dict = {}
    out["serviceId"] = value["service_id"]
    import capo_devops_agent.types.service_configuration

    out["configuration"] = capo_devops_agent.types.service_configuration.serialize_json(
        value["configuration"]
    )
    return out


def deserialize_json(data: dict) -> AssociateServiceInput:
    out: AssociateServiceInput = {}  # type: ignore[typeddict-item]
    if "serviceId" in data:
        out["service_id"] = data["serviceId"]
    else:
        raise DeserializationError("AssociateServiceInput.service_id required")
    if "configuration" in data:
        import capo_devops_agent.types.service_configuration

        out["configuration"] = (
            capo_devops_agent.types.service_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("AssociateServiceInput.configuration required")
    return out
