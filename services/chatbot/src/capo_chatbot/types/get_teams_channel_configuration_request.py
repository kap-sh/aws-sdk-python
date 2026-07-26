"""Generated from Smithy shape ``com.amazonaws.chatbot#GetTeamsChannelConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chatbot.types.chat_configuration_arn


class GetTeamsChannelConfigurationRequest(TypedDict, closed=True):
    chat_configuration_arn: (
        "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTeamsChannelConfigurationRequest) -> dict:
    out: dict = {}
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    return out


def deserialize_json(data: dict) -> GetTeamsChannelConfigurationRequest:
    out: GetTeamsChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ChatConfigurationArn" in data:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        raise DeserializationError(
            "GetTeamsChannelConfigurationRequest.chat_configuration_arn required"
        )
    return out
