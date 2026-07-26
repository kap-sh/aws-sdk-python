"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetChatResponseConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.chat_response_configuration_arn
    import capo_qbusiness.types.chat_response_configuration_detail
    import capo_qbusiness.types.chat_response_configuration_id
    import capo_qbusiness.types.display_name
    import capo_qbusiness.types.timestamp


class GetChatResponseConfigurationResponse(TypedDict, closed=True):
    chat_response_configuration_id: NotRequired[
        "capo_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId"
    ]
    """<p>The unique identifier of the retrieved chat response configuration.</p>"""
    chat_response_configuration_arn: NotRequired[
        "capo_qbusiness.types.chat_response_configuration_arn.ChatResponseConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the retrieved chat response configuration, which uniquely identifies the resource across all Amazon Web Services services. </p>"""
    display_name: NotRequired["capo_qbusiness.types.display_name.DisplayName"]
    """<p>The human-readable name of the retrieved chat response configuration, making it easier to identify among multiple configurations.</p>"""
    created_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp indicating when the chat response configuration was initially created.</p>"""
    in_use_configuration: NotRequired[
        "capo_qbusiness.types.chat_response_configuration_detail.ChatResponseConfigurationDetail"
    ]
    """<p>The currently active configuration settings that are being used to generate responses in the Amazon Q Business application.</p>"""
    last_update_configuration: NotRequired[
        "capo_qbusiness.types.chat_response_configuration_detail.ChatResponseConfigurationDetail"
    ]
    """<p>Information about the most recent update to the configuration, including timestamp and modification details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChatResponseConfigurationResponse) -> dict:
    out: dict = {}
    if "chat_response_configuration_id" in value:
        out["chatResponseConfigurationId"] = value["chat_response_configuration_id"]
    if "chat_response_configuration_arn" in value:
        out["chatResponseConfigurationArn"] = value["chat_response_configuration_arn"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "created_at" in value:
        import capo_qbusiness.types.timestamp

        out["createdAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "in_use_configuration" in value:
        import capo_qbusiness.types.chat_response_configuration_detail

        out["inUseConfiguration"] = (
            capo_qbusiness.types.chat_response_configuration_detail.serialize_json(
                value["in_use_configuration"]
            )
        )
    if "last_update_configuration" in value:
        import capo_qbusiness.types.chat_response_configuration_detail

        out["lastUpdateConfiguration"] = (
            capo_qbusiness.types.chat_response_configuration_detail.serialize_json(
                value["last_update_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetChatResponseConfigurationResponse:
    out: GetChatResponseConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "chatResponseConfigurationId" in data:
        out["chat_response_configuration_id"] = data["chatResponseConfigurationId"]
    if "chatResponseConfigurationArn" in data:
        out["chat_response_configuration_arn"] = data["chatResponseConfigurationArn"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "createdAt" in data:
        import capo_qbusiness.types.timestamp

        out["created_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "inUseConfiguration" in data:
        import capo_qbusiness.types.chat_response_configuration_detail

        out["in_use_configuration"] = (
            capo_qbusiness.types.chat_response_configuration_detail.deserialize_json(
                data["inUseConfiguration"]
            )
        )
    if "lastUpdateConfiguration" in data:
        import capo_qbusiness.types.chat_response_configuration_detail

        out["last_update_configuration"] = (
            capo_qbusiness.types.chat_response_configuration_detail.deserialize_json(
                data["lastUpdateConfiguration"]
            )
        )
    return out
