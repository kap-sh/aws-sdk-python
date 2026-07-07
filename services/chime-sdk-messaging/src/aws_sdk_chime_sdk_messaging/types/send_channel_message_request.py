"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SendChannelMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type
    import aws_sdk_chime_sdk_messaging.types.channel_message_type
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.client_request_token
    import aws_sdk_chime_sdk_messaging.types.content_type
    import aws_sdk_chime_sdk_messaging.types.message_attribute_map
    import aws_sdk_chime_sdk_messaging.types.metadata
    import aws_sdk_chime_sdk_messaging.types.non_empty_content
    import aws_sdk_chime_sdk_messaging.types.push_notification_configuration
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id
    import aws_sdk_chime_sdk_messaging.types.target_list


class SendChannelMessageRequest(TypedDict, closed=True):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    content: "aws_sdk_chime_sdk_messaging.types.non_empty_content.NonEmptyContent"
    """<p>The content of the channel message.</p>"""
    type: "aws_sdk_chime_sdk_messaging.types.channel_message_type.ChannelMessageType"
    """<p>The type of message, <code>STANDARD</code> or <code>CONTROL</code>.</p> <p> <code>STANDARD</code> messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.</p> <p> <code>CONTROL</code> messages are limited to 30 bytes and do not contain metadata.</p>"""
    persistence: "aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type.ChannelMessagePersistenceType"
    """<p>Boolean that controls whether the message is persisted on the back end. Required.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The optional metadata for each message.</p>"""
    client_request_token: (
        "aws_sdk_chime_sdk_messaging.types.client_request_token.ClientRequestToken"
    )
    """<p>The <code>Idempotency</code> token for each client request.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    push_notification: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.push_notification_configuration.PushNotificationConfiguration"
    ]
    """<p>The push notification configuration of the message.</p>"""
    message_attributes: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.message_attribute_map.MessageAttributeMap"
    ]
    """<p>The attributes for the message, used for message filtering along with a <code>FilterRule</code> defined in the <code>PushNotificationPreferences</code>.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p>"""
    content_type: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.content_type.ContentType"
    ]
    """<p>The content type of the channel message.</p>"""
    target: NotRequired["aws_sdk_chime_sdk_messaging.types.target_list.TargetList"]
    """<p>The target of a message. Must be a member of the channel, such as another user, a bot, or the sender. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendChannelMessageRequest) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    import aws_sdk_chime_sdk_messaging.types.channel_message_type

    out["Type"] = aws_sdk_chime_sdk_messaging.types.channel_message_type.serialize_json(
        value["type"]
    )
    import aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type

    out["Persistence"] = (
        aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type.serialize_json(
            value["persistence"]
        )
    )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    out["ClientRequestToken"] = value["client_request_token"]
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
    if "target" in value:
        import aws_sdk_chime_sdk_messaging.types.target_list

        out["Target"] = aws_sdk_chime_sdk_messaging.types.target_list.serialize_json(
            value["target"]
        )
    return out


def deserialize_json(data: dict) -> SendChannelMessageRequest:
    out: SendChannelMessageRequest = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("SendChannelMessageRequest.content required")
    if "Type" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_message_type

        out["type"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("SendChannelMessageRequest.type required")
    if "Persistence" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type

        out["persistence"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type.deserialize_json(
                data["Persistence"]
            )
        )
    else:
        raise DeserializationError("SendChannelMessageRequest.persistence required")
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError(
            "SendChannelMessageRequest.client_request_token required"
        )
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
    if "Target" in data:
        import aws_sdk_chime_sdk_messaging.types.target_list

        out["target"] = aws_sdk_chime_sdk_messaging.types.target_list.deserialize_json(
            data["Target"]
        )
    return out
