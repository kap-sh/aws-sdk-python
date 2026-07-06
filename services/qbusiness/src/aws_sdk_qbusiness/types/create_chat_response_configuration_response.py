"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateChatResponseConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.chat_response_configuration_arn
    import aws_sdk_qbusiness.types.chat_response_configuration_id


class CreateChatResponseConfigurationResponse(TypedDict, closed=True):
    chat_response_configuration_id: "aws_sdk_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId"
    """<p>The unique identifier assigned to a newly created chat response configuration, used for subsequent operations on this resource.</p>"""
    chat_response_configuration_arn: "aws_sdk_qbusiness.types.chat_response_configuration_arn.ChatResponseConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the newly created chat response configuration, which uniquely identifies the resource across all Amazon Web Services services. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChatResponseConfigurationResponse) -> dict:
    out: dict = {}
    out["chatResponseConfigurationId"] = value["chat_response_configuration_id"]
    out["chatResponseConfigurationArn"] = value["chat_response_configuration_arn"]
    return out


def deserialize_json(data: dict) -> CreateChatResponseConfigurationResponse:
    out: CreateChatResponseConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "chatResponseConfigurationId" in data:
        out["chat_response_configuration_id"] = data["chatResponseConfigurationId"]
    else:
        raise DeserializationError(
            "CreateChatResponseConfigurationResponse.chat_response_configuration_id required"
        )
    if "chatResponseConfigurationArn" in data:
        out["chat_response_configuration_arn"] = data["chatResponseConfigurationArn"]
    else:
        raise DeserializationError(
            "CreateChatResponseConfigurationResponse.chat_response_configuration_arn required"
        )
    return out
