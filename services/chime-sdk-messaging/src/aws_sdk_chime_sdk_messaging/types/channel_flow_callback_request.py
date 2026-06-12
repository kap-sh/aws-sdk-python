"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelFlowCallbackRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.callback_id_type
    import aws_sdk_chime_sdk_messaging.types.channel_message_callback
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.non_nullable_boolean


class ChannelFlowCallbackRequest(TypedDict):
    callback_id: "aws_sdk_chime_sdk_messaging.types.callback_id_type.CallbackIdType"
    """<p>The identifier passed to the processor by the service when invoked. Use the identifier to call back the service.</p>"""
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    delete_resource: (
        "aws_sdk_chime_sdk_messaging.types.non_nullable_boolean.NonNullableBoolean"
    )
    """<p>When a processor determines that a message needs to be <code>DENIED</code>, pass this parameter with a value of true.</p>"""
    channel_message: "aws_sdk_chime_sdk_messaging.types.channel_message_callback.ChannelMessageCallback"
    """<p>Stores information about the processed message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelFlowCallbackRequest) -> dict:
    out: dict = {}
    out["CallbackId"] = value["callback_id"]
    out["DeleteResource"] = value.get("delete_resource", False)
    import aws_sdk_chime_sdk_messaging.types.channel_message_callback

    out["ChannelMessage"] = (
        aws_sdk_chime_sdk_messaging.types.channel_message_callback.serialize_json(
            value["channel_message"]
        )
    )
    return out


def deserialize_json(data: dict) -> ChannelFlowCallbackRequest:
    out: ChannelFlowCallbackRequest = {}  # type: ignore[typeddict-item]
    if "CallbackId" in data:
        out["callback_id"] = data["CallbackId"]
    else:
        raise DeserializationError("ChannelFlowCallbackRequest.callback_id required")
    if "DeleteResource" in data:
        out["delete_resource"] = data["DeleteResource"]
    else:
        out["delete_resource"] = False
    if "ChannelMessage" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_message_callback

        out["channel_message"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_callback.deserialize_json(
                data["ChannelMessage"]
            )
        )
    else:
        raise DeserializationError(
            "ChannelFlowCallbackRequest.channel_message required"
        )
    return out
