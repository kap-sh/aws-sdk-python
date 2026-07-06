"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.asset_id_list
    import aws_sdk_devops_agent.types.chat_execution_id
    import aws_sdk_devops_agent.types.message_content
    import aws_sdk_devops_agent.types.resource_id
    import aws_sdk_devops_agent.types.send_message_context


class SendMessageRequest(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The agent space identifier</p>"""
    execution_id: "aws_sdk_devops_agent.types.chat_execution_id.ChatExecutionId"
    """<p>The execution identifier for the chat session</p>"""
    content: "aws_sdk_devops_agent.types.message_content.MessageContent"
    """<p>The user message content</p>"""
    context: NotRequired[
        "aws_sdk_devops_agent.types.send_message_context.SendMessageContext"
    ]
    """<p>Optional context for the message</p>"""
    user_id: NotRequired["aws_sdk_devops_agent.types.resource_id.ResourceId"]
    """<p>User identifier. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.</p>"""
    asset_ids: NotRequired["aws_sdk_devops_agent.types.asset_id_list.AssetIdList"]
    """<p>Optional list of asset identifiers to attach to the message</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageRequest) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    out["content"] = value["content"]
    if "context" in value:
        import aws_sdk_devops_agent.types.send_message_context

        out["context"] = aws_sdk_devops_agent.types.send_message_context.serialize_json(
            value["context"]
        )
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "asset_ids" in value:
        import aws_sdk_devops_agent.types.asset_id_list

        out["assetIds"] = aws_sdk_devops_agent.types.asset_id_list.serialize_json(
            value["asset_ids"]
        )
    return out


def deserialize_json(data: dict) -> SendMessageRequest:
    out: SendMessageRequest = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("SendMessageRequest.execution_id required")
    if "content" in data:
        out["content"] = data["content"]
    else:
        raise DeserializationError("SendMessageRequest.content required")
    if "context" in data:
        import aws_sdk_devops_agent.types.send_message_context

        out["context"] = (
            aws_sdk_devops_agent.types.send_message_context.deserialize_json(
                data["context"]
            )
        )
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "assetIds" in data:
        import aws_sdk_devops_agent.types.asset_id_list

        out["asset_ids"] = aws_sdk_devops_agent.types.asset_id_list.deserialize_json(
            data["assetIds"]
        )
    return out
