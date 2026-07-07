"""Generated from Smithy shape ``com.amazonaws.chatbot#AssociateToConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.chat_configuration_arn
    import aws_sdk_chatbot.types.resource_identifier


class AssociateToConfigurationRequest(TypedDict, closed=True):
    resource: "aws_sdk_chatbot.types.resource_identifier.ResourceIdentifier"
    """<p>The resource Amazon Resource Name (ARN) to link.</p>"""
    chat_configuration: (
        "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The channel configuration to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateToConfigurationRequest) -> dict:
    out: dict = {}
    out["Resource"] = value["resource"]
    out["ChatConfiguration"] = value["chat_configuration"]
    return out


def deserialize_json(data: dict) -> AssociateToConfigurationRequest:
    out: AssociateToConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "Resource" in data:
        out["resource"] = data["Resource"]
    else:
        raise DeserializationError("AssociateToConfigurationRequest.resource required")
    if "ChatConfiguration" in data:
        out["chat_configuration"] = data["ChatConfiguration"]
    else:
        raise DeserializationError(
            "AssociateToConfigurationRequest.chat_configuration required"
        )
    return out
