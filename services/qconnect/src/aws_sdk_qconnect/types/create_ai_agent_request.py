"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIAgentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_configuration
    import aws_sdk_qconnect.types.ai_agent_type
    import aws_sdk_qconnect.types.client_token
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.visibility_status


class CreateAIAgentRequest(TypedDict):
    client_token: NotRequired["aws_sdk_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>..</p>"""
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The name of the AI Agent.</p>"""
    type: "aws_sdk_qconnect.types.ai_agent_type.AIAgentType"
    """<p>The type of the AI Agent.</p>"""
    configuration: "aws_sdk_qconnect.types.ai_agent_configuration.AIAgentConfiguration"
    """<p>The configuration of the AI Agent.</p>"""
    visibility_status: "aws_sdk_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Agent.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description of the AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIAgentRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    import aws_sdk_qconnect.types.ai_agent_configuration

    out["configuration"] = aws_sdk_qconnect.types.ai_agent_configuration.serialize_json(
        value["configuration"]
    )
    out["visibilityStatus"] = value["visibility_status"]
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateAIAgentRequest:
    out: CreateAIAgentRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAIAgentRequest.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateAIAgentRequest.type required")
    if "configuration" in data:
        import aws_sdk_qconnect.types.ai_agent_configuration

        out["configuration"] = (
            aws_sdk_qconnect.types.ai_agent_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateAIAgentRequest.configuration required")
    if "visibilityStatus" in data:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("CreateAIAgentRequest.visibility_status required")
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    if "description" in data:
        out["description"] = data["description"]
    return out
