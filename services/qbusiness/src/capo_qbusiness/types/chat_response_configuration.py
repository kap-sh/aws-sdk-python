"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatResponseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.chat_response_configuration_arn
    import capo_qbusiness.types.chat_response_configuration_id
    import capo_qbusiness.types.chat_response_configuration_status
    import capo_qbusiness.types.display_name
    import capo_qbusiness.types.response_configuration_summary
    import capo_qbusiness.types.timestamp


class ChatResponseConfiguration(TypedDict, closed=True):
    chat_response_configuration_id: "capo_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId"
    """<p>A unique identifier for your chat response configuration settings, used to reference and manage the configuration within the Amazon Q Business service.</p>"""
    chat_response_configuration_arn: "capo_qbusiness.types.chat_response_configuration_arn.ChatResponseConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the chat response configuration, which uniquely identifies the resource across all Amazon Web Services services and accounts.</p>"""
    display_name: "capo_qbusiness.types.display_name.DisplayName"
    """<p>A human-readable name for the chat response configuration, making it easier to identify and manage multiple configurations within an organization.</p>"""
    response_configuration_summary: NotRequired[
        "capo_qbusiness.types.response_configuration_summary.ResponseConfigurationSummary"
    ]
    """<p>A summary of the response configuration settings, providing a concise overview of the key parameters that define how responses are generated and formatted.</p>"""
    status: "capo_qbusiness.types.chat_response_configuration_status.ChatResponseConfigurationStatus"
    """<p>The current status of the chat response configuration, indicating whether it is active, pending, or in another state that affects its availability for use in chat interactions.</p>"""
    created_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp indicating when the chat response configuration was initially created, useful for tracking the lifecycle of configuration resources.</p>"""
    updated_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp indicating when the chat response configuration was last modified, helping administrators track changes and maintain version awareness.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatResponseConfiguration) -> dict:
    out: dict = {}
    out["chatResponseConfigurationId"] = value["chat_response_configuration_id"]
    out["chatResponseConfigurationArn"] = value["chat_response_configuration_arn"]
    out["displayName"] = value["display_name"]
    if "response_configuration_summary" in value:
        out["responseConfigurationSummary"] = value["response_configuration_summary"]
    import capo_qbusiness.types.chat_response_configuration_status

    out["status"] = (
        capo_qbusiness.types.chat_response_configuration_status.serialize_json(
            value["status"]
        )
    )
    if "created_at" in value:
        import capo_qbusiness.types.timestamp

        out["createdAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_qbusiness.types.timestamp

        out["updatedAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ChatResponseConfiguration:
    out: ChatResponseConfiguration = {}  # type: ignore[typeddict-item]
    if "chatResponseConfigurationId" in data:
        out["chat_response_configuration_id"] = data["chatResponseConfigurationId"]
    else:
        raise DeserializationError(
            "ChatResponseConfiguration.chat_response_configuration_id required"
        )
    if "chatResponseConfigurationArn" in data:
        out["chat_response_configuration_arn"] = data["chatResponseConfigurationArn"]
    else:
        raise DeserializationError(
            "ChatResponseConfiguration.chat_response_configuration_arn required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("ChatResponseConfiguration.display_name required")
    if "responseConfigurationSummary" in data:
        out["response_configuration_summary"] = data["responseConfigurationSummary"]
    if "status" in data:
        import capo_qbusiness.types.chat_response_configuration_status

        out["status"] = (
            capo_qbusiness.types.chat_response_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ChatResponseConfiguration.status required")
    if "createdAt" in data:
        import capo_qbusiness.types.timestamp

        out["created_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_qbusiness.types.timestamp

        out["updated_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
