"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type
    import aws_sdk_chime_sdk_messaging.types.channel_message_status_structure
    import aws_sdk_chime_sdk_messaging.types.channel_message_type
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.content
    import aws_sdk_chime_sdk_messaging.types.content_type
    import aws_sdk_chime_sdk_messaging.types.identity
    import aws_sdk_chime_sdk_messaging.types.message_attribute_map
    import aws_sdk_chime_sdk_messaging.types.message_id
    import aws_sdk_chime_sdk_messaging.types.metadata
    import aws_sdk_chime_sdk_messaging.types.non_nullable_boolean
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id
    import aws_sdk_chime_sdk_messaging.types.target_list
    import aws_sdk_chime_sdk_messaging.types.timestamp


class ChannelMessage(TypedDict):
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    message_id: NotRequired["aws_sdk_chime_sdk_messaging.types.message_id.MessageId"]
    """<p>The ID of a message.</p>"""
    content: NotRequired["aws_sdk_chime_sdk_messaging.types.content.Content"]
    r"""<p>The content of the channel message. For Amazon Lex V2 bot responses, this field holds a list of messages originating from the bot. For more information, refer to <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html\">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The message metadata.</p>"""
    type: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_message_type.ChannelMessageType"
    ]
    """<p>The message type.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which the message was created.</p>"""
    last_edited_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a message was edited.</p>"""
    last_updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a message was updated.</p>"""
    sender: NotRequired["aws_sdk_chime_sdk_messaging.types.identity.Identity"]
    """<p>The message sender.</p>"""
    redacted: (
        "aws_sdk_chime_sdk_messaging.types.non_nullable_boolean.NonNullableBoolean"
    )
    """<p>Hides the content of a message.</p>"""
    persistence: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type.ChannelMessagePersistenceType"
    ]
    """<p>The persistence setting for a channel message.</p>"""
    status: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_message_status_structure.ChannelMessageStatusStructure"
    ]
    """<p>The status of the channel message.</p>"""
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
    r"""<p>The content type of the channel message. For Amazon Lex V2 bot responses, the content type is <code>application/amz-chime-lex-msgs</code> for success responses and <code>application/amz-chime-lex-error</code> for failure responses. For more information, refer to <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html\">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    target: NotRequired["aws_sdk_chime_sdk_messaging.types.target_list.TargetList"]
    """<p>The target of a message, a sender, a user, or a bot. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessage) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "content" in value:
        out["Content"] = value["content"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "type" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_message_type

        out["Type"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_type.serialize_json(
                value["type"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_edited_timestamp" in value:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["LastEditedTimestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_edited_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["LastUpdatedTimestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "sender" in value:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["Sender"] = aws_sdk_chime_sdk_messaging.types.identity.serialize_json(
            value["sender"]
        )
    out["Redacted"] = value.get("redacted", False)
    if "persistence" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type

        out["Persistence"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type.serialize_json(
                value["persistence"]
            )
        )
    if "status" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_message_status_structure

        out["Status"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_status_structure.serialize_json(
                value["status"]
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


def deserialize_json(data: dict) -> ChannelMessage:
    out: ChannelMessage = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    if "Type" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_message_type

        out["type"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_type.deserialize_json(
                data["Type"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "LastEditedTimestamp" in data:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["last_edited_timestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastEditedTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if "Sender" in data:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["sender"] = aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(
            data["Sender"]
        )
    if "Redacted" in data:
        out["redacted"] = data["Redacted"]
    else:
        out["redacted"] = False
    if "Persistence" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type

        out["persistence"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type.deserialize_json(
                data["Persistence"]
            )
        )
    if "Status" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_message_status_structure

        out["status"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_status_structure.deserialize_json(
                data["Status"]
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
