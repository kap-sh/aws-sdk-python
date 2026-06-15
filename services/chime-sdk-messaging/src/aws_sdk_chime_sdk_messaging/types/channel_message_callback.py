"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessageCallback``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.content_type
    import aws_sdk_chime_sdk_messaging.types.message_attribute_map
    import aws_sdk_chime_sdk_messaging.types.message_id
    import aws_sdk_chime_sdk_messaging.types.metadata
    import aws_sdk_chime_sdk_messaging.types.non_empty_content
    import aws_sdk_chime_sdk_messaging.types.push_notification_configuration
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id


class ChannelMessageCallback(TypedDict):
    message_id: "aws_sdk_chime_sdk_messaging.types.message_id.MessageId"
    """<p>The message ID.</p>"""
    content: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.non_empty_content.NonEmptyContent"
    ]
    r"""<p>The message content. For Amazon Lex V2 bot responses, this field holds a list of messages originating from the bot. For more information, refer to <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html\">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The message metadata.</p>"""
    push_notification: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.push_notification_configuration.PushNotificationConfiguration"
    ]
    """<p>The push notification configuration of the message.</p>"""
    message_attributes: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.message_attribute_map.MessageAttributeMap"
    ]
    r"""<p>The attributes for the channel message. For Amazon Lex V2 bot responses, the attributes are mapped to specific fields from the bot. For more information, refer to <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html\">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel.</p>"""
    content_type: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.content_type.ContentType"
    ]
    r"""<p>The content type of the call-back message. For Amazon Lex V2 bot responses, the content type is <code>application/amz-chime-lex-msgs</code> for success responses and <code>application/amz-chime-lex-error</code> for failure responses. For more information, refer to <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html\">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessageCallback) -> dict:
    out: dict = {}
    out["MessageId"] = value["message_id"]
    if "content" in value:
        out["Content"] = value["content"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "push_notification" in value:
        import aws_sdk_chime_sdk_messaging.types.push_notification_configuration

        out["PushNotification"] = (
            aws_sdk_chime_sdk_messaging.types.push_notification_configuration.serialize_json(
                value["push_notification"]
            )
        )
    if "message_attributes" in value:
        import aws_sdk_chime_sdk_messaging.types.message_attribute_map

        out["MessageAttributes"] = (
            aws_sdk_chime_sdk_messaging.types.message_attribute_map.serialize_json(
                value["message_attributes"]
            )
        )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> ChannelMessageCallback:
    out: ChannelMessageCallback = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    else:
        raise DeserializationError("ChannelMessageCallback.message_id required")
    if "Content" in data:
        out["content"] = data["Content"]
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    if "PushNotification" in data:
        import aws_sdk_chime_sdk_messaging.types.push_notification_configuration

        out["push_notification"] = (
            aws_sdk_chime_sdk_messaging.types.push_notification_configuration.deserialize_json(
                data["PushNotification"]
            )
        )
    if "MessageAttributes" in data:
        import aws_sdk_chime_sdk_messaging.types.message_attribute_map

        out["message_attributes"] = (
            aws_sdk_chime_sdk_messaging.types.message_attribute_map.deserialize_json(
                data["MessageAttributes"]
            )
        )
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    return out
