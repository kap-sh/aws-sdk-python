"""Generated from Smithy shape ``com.amazonaws.qconnect#SendMessageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_configuration
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.uuid


class SendMessageResponse(TypedDict):
    request_message_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the submitted message.</p>"""
    configuration: NotRequired[
        "aws_sdk_qconnect.types.message_configuration.MessageConfiguration"
    ]
    r"""<p>The configuration of the <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SendMessage.html\">SendMessage</a> request.</p>"""
    next_message_token: "aws_sdk_qconnect.types.next_token.NextToken"
    """<p>The token for the next message, used by GetNextMessage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageResponse) -> dict:
    out: dict = {}
    out["requestMessageId"] = value["request_message_id"]
    if "configuration" in value:
        import aws_sdk_qconnect.types.message_configuration

        out["configuration"] = (
            aws_sdk_qconnect.types.message_configuration.serialize_json(
                value["configuration"]
            )
        )
    out["nextMessageToken"] = value["next_message_token"]
    return out


def deserialize_json(data: dict) -> SendMessageResponse:
    out: SendMessageResponse = {}  # type: ignore[typeddict-item]
    if "requestMessageId" in data:
        out["request_message_id"] = data["requestMessageId"]
    else:
        raise DeserializationError("SendMessageResponse.request_message_id required")
    if "configuration" in data:
        import aws_sdk_qconnect.types.message_configuration

        out["configuration"] = (
            aws_sdk_qconnect.types.message_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "nextMessageToken" in data:
        out["next_message_token"] = data["nextMessageToken"]
    else:
        raise DeserializationError("SendMessageResponse.next_message_token required")
    return out
