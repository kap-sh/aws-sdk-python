"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UpdateChannelMessageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.content_type
    import aws_sdk_chime_sdk_messaging.types.message_id
    import aws_sdk_chime_sdk_messaging.types.metadata
    import aws_sdk_chime_sdk_messaging.types.non_empty_content
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id


class UpdateChannelMessageRequest(TypedDict):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    message_id: "aws_sdk_chime_sdk_messaging.types.message_id.MessageId"
    """<p>The ID string of the message being updated.</p>"""
    content: "aws_sdk_chime_sdk_messaging.types.non_empty_content.NonEmptyContent"
    """<p>The content of the channel message. </p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The metadata of the message being updated.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p> <note> <p>Only required when updating messages in a SubChannel that the user belongs to.</p> </note>"""
    content_type: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.content_type.ContentType"
    ]
    """<p>The content type of the channel message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelMessageRequest) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> UpdateChannelMessageRequest:
    out: UpdateChannelMessageRequest = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("UpdateChannelMessageRequest.content required")
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    return out
