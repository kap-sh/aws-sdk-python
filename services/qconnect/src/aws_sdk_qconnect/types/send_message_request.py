"""Generated from Smithy shape ``com.amazonaws.qconnect#SendMessageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.client_token
    import aws_sdk_qconnect.types.conversation_context
    import aws_sdk_qconnect.types.message_configuration
    import aws_sdk_qconnect.types.message_input
    import aws_sdk_qconnect.types.message_metadata
    import aws_sdk_qconnect.types.message_type
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier


class SendMessageRequest(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    session_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect session.</p>"""
    type: "aws_sdk_qconnect.types.message_type.MessageType"
    """<p>The message type.</p>"""
    message: "aws_sdk_qconnect.types.message_input.MessageInput"
    """<p>The message data to submit to the Amazon Q in Connect session.</p>"""
    ai_agent_id: NotRequired[
        "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    ]
    """<p>The identifier of the AI Agent to use for processing the message.</p>"""
    conversation_context: NotRequired[
        "aws_sdk_qconnect.types.conversation_context.ConversationContext"
    ]
    """<p>The conversation context before the Amazon Q in Connect session.</p>"""
    configuration: NotRequired[
        "aws_sdk_qconnect.types.message_configuration.MessageConfiguration"
    ]
    """<p>The configuration of the <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SendMessage.html\">SendMessage</a> request.</p>"""
    client_token: NotRequired["aws_sdk_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field.For more information about idempotency, see Making retries safe with idempotent APIs.</p>"""
    orchestrator_use_case: NotRequired[
        "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>The orchestrator use case for message processing.</p>"""
    metadata: NotRequired["aws_sdk_qconnect.types.message_metadata.MessageMetadata"]
    """<p>Additional metadata for the message.</p>"""
    origin_request_id: NotRequired[
        "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """Request identifier from the origin system, used for end-to-end tracing across spans."""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import aws_sdk_qconnect.types.message_input

    out["message"] = aws_sdk_qconnect.types.message_input.serialize_json(
        value["message"]
    )
    if "ai_agent_id" in value:
        out["aiAgentId"] = value["ai_agent_id"]
    if "conversation_context" in value:
        import aws_sdk_qconnect.types.conversation_context

        out["conversationContext"] = (
            aws_sdk_qconnect.types.conversation_context.serialize_json(
                value["conversation_context"]
            )
        )
    if "configuration" in value:
        import aws_sdk_qconnect.types.message_configuration

        out["configuration"] = (
            aws_sdk_qconnect.types.message_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "orchestrator_use_case" in value:
        out["orchestratorUseCase"] = value["orchestrator_use_case"]
    if "metadata" in value:
        import aws_sdk_qconnect.types.message_metadata

        out["metadata"] = aws_sdk_qconnect.types.message_metadata.serialize_json(
            value["metadata"]
        )
    if "origin_request_id" in value:
        out["originRequestId"] = value["origin_request_id"]
    return out


def deserialize_json(data: dict) -> SendMessageRequest:
    out: SendMessageRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SendMessageRequest.type required")
    if "message" in data:
        import aws_sdk_qconnect.types.message_input

        out["message"] = aws_sdk_qconnect.types.message_input.deserialize_json(
            data["message"]
        )
    else:
        raise DeserializationError("SendMessageRequest.message required")
    if "aiAgentId" in data:
        out["ai_agent_id"] = data["aiAgentId"]
    if "conversationContext" in data:
        import aws_sdk_qconnect.types.conversation_context

        out["conversation_context"] = (
            aws_sdk_qconnect.types.conversation_context.deserialize_json(
                data["conversationContext"]
            )
        )
    if "configuration" in data:
        import aws_sdk_qconnect.types.message_configuration

        out["configuration"] = (
            aws_sdk_qconnect.types.message_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "orchestratorUseCase" in data:
        out["orchestrator_use_case"] = data["orchestratorUseCase"]
    if "metadata" in data:
        import aws_sdk_qconnect.types.message_metadata

        out["metadata"] = aws_sdk_qconnect.types.message_metadata.deserialize_json(
            data["metadata"]
        )
    if "originRequestId" in data:
        out["origin_request_id"] = data["originRequestId"]
    return out
