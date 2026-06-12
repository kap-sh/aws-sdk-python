"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteChatResponseConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.chat_response_configuration_id

class DeleteChatResponseConfigurationRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of theAmazon Q Business application from which to delete the chat response configuration.</p>"""
    chat_response_configuration_id: "aws_sdk_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId"
    """<p>The unique identifier of the chat response configuration to delete from the specified application. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteChatResponseConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChatResponseConfigurationRequest:
    out: DeleteChatResponseConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out