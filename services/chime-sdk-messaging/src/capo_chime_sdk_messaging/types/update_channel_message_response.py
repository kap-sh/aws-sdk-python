"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UpdateChannelMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_message_status_structure
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.message_id
    import capo_chime_sdk_messaging.types.sub_channel_id


class UpdateChannelMessageResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    message_id: NotRequired["capo_chime_sdk_messaging.types.message_id.MessageId"]
    """<p>The ID string of the message being updated.</p>"""
    status: NotRequired[
        "capo_chime_sdk_messaging.types.channel_message_status_structure.ChannelMessageStatusStructure"
    ]
    """<p>The status of the message update.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelMessageResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "status" in value:
        import capo_chime_sdk_messaging.types.channel_message_status_structure

        out["Status"] = (
            capo_chime_sdk_messaging.types.channel_message_status_structure.serialize_json(
                value["status"]
            )
        )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> UpdateChannelMessageResponse:
    out: UpdateChannelMessageResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    if "Status" in data:
        import capo_chime_sdk_messaging.types.channel_message_status_structure

        out["status"] = (
            capo_chime_sdk_messaging.types.channel_message_status_structure.deserialize_json(
                data["Status"]
            )
        )
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
