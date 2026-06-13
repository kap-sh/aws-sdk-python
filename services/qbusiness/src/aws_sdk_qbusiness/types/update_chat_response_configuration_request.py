"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateChatResponseConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.chat_response_configuration_id
    import aws_sdk_qbusiness.types.display_name
    import aws_sdk_qbusiness.types.response_configurations
    import aws_sdk_qbusiness.types.string


class UpdateChatResponseConfigurationRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application containing the chat response configuration to update.</p>"""
    chat_response_configuration_id: "aws_sdk_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId"
    """<p>The unique identifier of the chat response configuration to update within the specified application.</p>"""
    display_name: NotRequired["aws_sdk_qbusiness.types.display_name.DisplayName"]
    """<p>The new human-readable name to assign to the chat response configuration, making it easier to identify among multiple configurations.</p>"""
    response_configurations: (
        "aws_sdk_qbusiness.types.response_configurations.ResponseConfigurations"
    )
    """<p>The updated collection of response configuration settings that define how Amazon Q Business generates and formats responses to user queries.</p>"""
    client_token: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This helps prevent the same update from being processed multiple times if retries occur.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChatResponseConfigurationRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    import aws_sdk_qbusiness.types.response_configurations

    out["responseConfigurations"] = (
        aws_sdk_qbusiness.types.response_configurations.serialize_json(
            value["response_configurations"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateChatResponseConfigurationRequest:
    out: UpdateChatResponseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "responseConfigurations" in data:
        import aws_sdk_qbusiness.types.response_configurations

        out["response_configurations"] = (
            aws_sdk_qbusiness.types.response_configurations.deserialize_json(
                data["responseConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateChatResponseConfigurationRequest.response_configurations required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
