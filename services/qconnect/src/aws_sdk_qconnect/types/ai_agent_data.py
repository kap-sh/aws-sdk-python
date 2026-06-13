"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.ai_agent_configuration
    import aws_sdk_qconnect.types.ai_agent_type
    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.origin
    import aws_sdk_qconnect.types.status
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid
    import aws_sdk_qconnect.types.visibility_status


class AIAgentData(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    assistant_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    ai_agent_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the AI Agent.</p>"""
    ai_agent_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the AI agent.</p>"""
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The name of the AI Agent.</p>"""
    type: "aws_sdk_qconnect.types.ai_agent_type.AIAgentType"
    """<p>The type of the AI Agent.</p>"""
    configuration: "aws_sdk_qconnect.types.ai_agent_configuration.AIAgentConfiguration"
    """<p>Configuration for the AI Agent.</p>"""
    modified_time: NotRequired["datetime.datetime"]
    """<p>The time the AI Agent was last modified.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description of the AI Agent.</p>"""
    visibility_status: "aws_sdk_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Agent.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    origin: NotRequired["aws_sdk_qconnect.types.origin.Origin"]
    """<p>Specifies the origin of the AI Agent. <code>SYSTEM</code> for a default AI Agent created by Q in Connect or <code>CUSTOMER</code> for an AI Agent created by calling AI Agent creation APIs. </p>"""
    status: NotRequired["aws_sdk_qconnect.types.status.Status"]
    """<p>The status of the AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentData) -> dict:
    out: dict = {}
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["aiAgentId"] = value["ai_agent_id"]
    out["aiAgentArn"] = value["ai_agent_arn"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    import aws_sdk_qconnect.types.ai_agent_configuration

    out["configuration"] = aws_sdk_qconnect.types.ai_agent_configuration.serialize_json(
        value["configuration"]
    )
    if "modified_time" in value:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["modifiedTime"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
            value["modified_time"]
        )
    if "description" in value:
        out["description"] = value["description"]
    out["visibilityStatus"] = value["visibility_status"]
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    if "origin" in value:
        out["origin"] = value["origin"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AIAgentData:
    out: AIAgentData = {}  # type: ignore[typeddict-item]
    if "assistantId" in data:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("AIAgentData.assistant_id required")
    if "assistantArn" in data:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("AIAgentData.assistant_arn required")
    if "aiAgentId" in data:
        out["ai_agent_id"] = data["aiAgentId"]
    else:
        raise DeserializationError("AIAgentData.ai_agent_id required")
    if "aiAgentArn" in data:
        out["ai_agent_arn"] = data["aiAgentArn"]
    else:
        raise DeserializationError("AIAgentData.ai_agent_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AIAgentData.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AIAgentData.type required")
    if "configuration" in data:
        import aws_sdk_qconnect.types.ai_agent_configuration

        out["configuration"] = (
            aws_sdk_qconnect.types.ai_agent_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("AIAgentData.configuration required")
    if "modifiedTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["modified_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["modifiedTime"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "visibilityStatus" in data:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("AIAgentData.visibility_status required")
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    if "origin" in data:
        out["origin"] = data["origin"]
    if "status" in data:
        out["status"] = data["status"]
    return out
