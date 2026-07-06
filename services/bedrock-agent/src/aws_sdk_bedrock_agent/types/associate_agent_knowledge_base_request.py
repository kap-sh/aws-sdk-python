"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AssociateAgentKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.draft_version
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.knowledge_base_state


class AssociateAgentKnowledgeBaseRequest(TypedDict, closed=True):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent with which you want to associate the knowledge base.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The version of the agent with which you want to associate the knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to associate with the agent.</p>"""
    description: "aws_sdk_bedrock_agent.types.description.Description"
    """<p>A description of what the agent should use the knowledge base for.</p>"""
    knowledge_base_state: NotRequired[
        "aws_sdk_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
    ]
    r"""<p>Specifies whether to use the knowledge base or not when sending an <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html\">InvokeAgent</a> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAgentKnowledgeBaseRequest) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["description"] = value["description"]
    if "knowledge_base_state" in value:
        import aws_sdk_bedrock_agent.types.knowledge_base_state

        out["knowledgeBaseState"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_state.serialize_json(
                value["knowledge_base_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateAgentKnowledgeBaseRequest:
    out: AssociateAgentKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "AssociateAgentKnowledgeBaseRequest.knowledge_base_id required"
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "AssociateAgentKnowledgeBaseRequest.description required"
        )
    if "knowledgeBaseState" in data:
        import aws_sdk_bedrock_agent.types.knowledge_base_state

        out["knowledge_base_state"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_state.deserialize_json(
                data["knowledgeBaseState"]
            )
        )
    return out
