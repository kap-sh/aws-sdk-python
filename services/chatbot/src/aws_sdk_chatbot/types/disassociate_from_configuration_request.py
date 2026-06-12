"""Generated from Smithy shape ``com.amazonaws.chatbot#DisassociateFromConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.chat_configuration_arn
    import aws_sdk_chatbot.types.resource_identifier


class DisassociateFromConfigurationRequest(TypedDict):
    resource: "aws_sdk_chatbot.types.resource_identifier.ResourceIdentifier"
    """<p>The resource (for example, a custom action) Amazon Resource Name (ARN) to unlink.</p>"""
    chat_configuration: (
        "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The channel configuration the resource is being disassociated from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateFromConfigurationRequest) -> dict:
    out: dict = {}
    out["Resource"] = value["resource"]
    out["ChatConfiguration"] = value["chat_configuration"]
    return out


def deserialize_json(data: dict) -> DisassociateFromConfigurationRequest:
    out: DisassociateFromConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "Resource" in data:
        out["resource"] = data["Resource"]
    else:
        raise DeserializationError(
            "DisassociateFromConfigurationRequest.resource required"
        )
    if "ChatConfiguration" in data:
        out["chat_configuration"] = data["ChatConfiguration"]
    else:
        raise DeserializationError(
            "DisassociateFromConfigurationRequest.chat_configuration required"
        )
    return out
