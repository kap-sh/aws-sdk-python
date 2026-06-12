"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteTeamsChannelConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.chat_configuration_arn


class DeleteTeamsChannelConfigurationRequest(TypedDict):
    chat_configuration_arn: (
        "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTeamsChannelConfigurationRequest) -> dict:
    out: dict = {}
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DeleteTeamsChannelConfigurationRequest:
    out: DeleteTeamsChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ChatConfigurationArn" in data:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        raise DeserializationError(
            "DeleteTeamsChannelConfigurationRequest.chat_configuration_arn required"
        )
    return out
