"""Generated from Smithy shape ``com.amazonaws.devopsagent#AgentSpace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.agent_space_name
    import aws_sdk_devops_agent.types.description
    import aws_sdk_devops_agent.types.kms_key_arn
    import aws_sdk_devops_agent.types.locale


class AgentSpace(TypedDict):
    name: "aws_sdk_devops_agent.types.agent_space_name.AgentSpaceName"
    """<p>The name of the AgentSpace.</p>"""
    description: NotRequired["aws_sdk_devops_agent.types.description.Description"]
    """<p>The description of the AgentSpace.</p>"""
    locale: NotRequired["aws_sdk_devops_agent.types.locale.Locale"]
    """<p>The locale for the AgentSpace, which determines the language used in agent responses.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the resource was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the resource was last updated.</p>"""
    kms_key_arn: NotRequired["aws_sdk_devops_agent.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>"""
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpace) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "locale" in value:
        out["locale"] = value["locale"]
    import aws_sdk_devops_agent.types._prelude.timestamp

    out["createdAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_devops_agent.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> AgentSpace:
    out: AgentSpace = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AgentSpace.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "locale" in data:
        out["locale"] = data["locale"]
    if "createdAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("AgentSpace.created_at required")
    if "updatedAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("AgentSpace.updated_at required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("AgentSpace.agent_space_id required")
    return out
