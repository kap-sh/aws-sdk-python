"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetChatResponseConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.chat_response_configuration_id


class GetChatResponseConfigurationRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application containing the chat response configuration to retrieve.</p>"""
    chat_response_configuration_id: "aws_sdk_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId"
    """<p>The unique identifier of the chat response configuration to retrieve from the specified application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChatResponseConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChatResponseConfigurationRequest:
    out: GetChatResponseConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
