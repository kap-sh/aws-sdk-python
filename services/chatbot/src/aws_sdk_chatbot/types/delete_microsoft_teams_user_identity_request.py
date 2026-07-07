"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteMicrosoftTeamsUserIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.chat_configuration_arn
    import aws_sdk_chatbot.types.uuid


class DeleteMicrosoftTeamsUserIdentityRequest(TypedDict, closed=True):
    chat_configuration_arn: (
        "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The ARN of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.</p>"""
    user_id: "aws_sdk_chatbot.types.uuid.UUID"
    """<p>The Microsoft Teams user ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMicrosoftTeamsUserIdentityRequest) -> dict:
    out: dict = {}
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    out["UserId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> DeleteMicrosoftTeamsUserIdentityRequest:
    out: DeleteMicrosoftTeamsUserIdentityRequest = {}  # type: ignore[typeddict-item]
    if "ChatConfigurationArn" in data:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        raise DeserializationError(
            "DeleteMicrosoftTeamsUserIdentityRequest.chat_configuration_arn required"
        )
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError(
            "DeleteMicrosoftTeamsUserIdentityRequest.user_id required"
        )
    return out
