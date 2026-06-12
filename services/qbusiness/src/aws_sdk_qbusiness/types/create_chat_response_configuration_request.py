"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateChatResponseConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_qbusiness.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.display_name
    import aws_sdk_qbusiness.types.response_configurations
    import aws_sdk_qbusiness.types.string
    import aws_sdk_qbusiness.types.tags

class CreateChatResponseConfigurationRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application for which to create the new chat response configuration.</p>"""
    display_name: "aws_sdk_qbusiness.types.display_name.DisplayName"
    """<p>A human-readable name for the new chat response configuration, making it easier to identify and manage among multiple configurations.</p>"""
    client_token: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This helps prevent the same configuration from being created multiple times if retries occur.</p>"""
    response_configurations: "aws_sdk_qbusiness.types.response_configurations.ResponseConfigurations"
    """<p>A collection of response configuration settings that define how Amazon Q Business will generate and format responses to user queries in chat interactions.</p>"""
    tags: NotRequired["aws_sdk_qbusiness.types.tags.Tags"]
    """<p>A list of key-value pairs to apply as tags to the new chat response configuration, enabling categorization and management of resources across Amazon Web Services services.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateChatResponseConfigurationRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_qbusiness.types.response_configurations
    out["responseConfigurations"] = aws_sdk_qbusiness.types.response_configurations.serialize_json(value["response_configurations"])
    if "tags" in value:
        import aws_sdk_qbusiness.types.tags
        out["tags"] = aws_sdk_qbusiness.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateChatResponseConfigurationRequest:
    out: CreateChatResponseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateChatResponseConfigurationRequest.display_name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "responseConfigurations" in data:
        import aws_sdk_qbusiness.types.response_configurations
        out["response_configurations"] = aws_sdk_qbusiness.types.response_configurations.deserialize_json(data["responseConfigurations"])
    else:
        raise DeserializationError("CreateChatResponseConfigurationRequest.response_configurations required")
    if "tags" in data:
        import aws_sdk_qbusiness.types.tags
        out["tags"] = aws_sdk_qbusiness.types.tags.deserialize_json(data["tags"])
    return out