"""Generated from Smithy shape ``com.amazonaws.devopsagent#Association``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.association_id
    import aws_sdk_devops_agent.types.service_configuration
    import aws_sdk_devops_agent.types.service_id
    import aws_sdk_devops_agent.types.validation_status


class Association(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the resource was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the resource was last updated.</p>"""
    status: NotRequired["aws_sdk_devops_agent.types.validation_status.ValidationStatus"]
    """<p>Validation status</p>"""
    association_id: "aws_sdk_devops_agent.types.association_id.AssociationId"
    """<p>The unique identifier of the given association.</p>"""
    service_id: "aws_sdk_devops_agent.types.service_id.ServiceId"
    """<p>The identifier for associated service</p>"""
    configuration: (
        "aws_sdk_devops_agent.types.service_configuration.ServiceConfiguration"
    )
    """<p>The configuration that directs how AgentSpace interacts with the given service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Association) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import aws_sdk_devops_agent.types._prelude.timestamp

    out["createdAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_devops_agent.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "status" in value:
        import aws_sdk_devops_agent.types.validation_status

        out["status"] = aws_sdk_devops_agent.types.validation_status.serialize_json(
            value["status"]
        )
    out["associationId"] = value["association_id"]
    out["serviceId"] = value["service_id"]
    import aws_sdk_devops_agent.types.service_configuration

    out["configuration"] = (
        aws_sdk_devops_agent.types.service_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> Association:
    out: Association = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("Association.agent_space_id required")
    if "createdAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Association.created_at required")
    if "updatedAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("Association.updated_at required")
    if "status" in data:
        import aws_sdk_devops_agent.types.validation_status

        out["status"] = aws_sdk_devops_agent.types.validation_status.deserialize_json(
            data["status"]
        )
    if "associationId" in data:
        out["association_id"] = data["associationId"]
    else:
        raise DeserializationError("Association.association_id required")
    if "serviceId" in data:
        out["service_id"] = data["serviceId"]
    else:
        raise DeserializationError("Association.service_id required")
    if "configuration" in data:
        import aws_sdk_devops_agent.types.service_configuration

        out["configuration"] = (
            aws_sdk_devops_agent.types.service_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("Association.configuration required")
    return out
