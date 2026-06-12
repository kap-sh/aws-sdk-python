"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessageStatusStructure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_message_status
    import aws_sdk_chime_sdk_messaging.types.status_detail


class ChannelMessageStatusStructure(TypedDict):
    value: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_message_status.ChannelMessageStatus"
    ]
    """<p>The message status value.</p>"""
    detail: NotRequired["aws_sdk_chime_sdk_messaging.types.status_detail.StatusDetail"]
    """<p>Contains more details about the message status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessageStatusStructure) -> dict:
    out: dict = {}
    if "value" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_message_status

        out["Value"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_status.serialize_json(
                value["value"]
            )
        )
    if "detail" in value:
        out["Detail"] = value["detail"]
    return out


def deserialize_json(data: dict) -> ChannelMessageStatusStructure:
    out: ChannelMessageStatusStructure = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_message_status

        out["value"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_status.deserialize_json(
                data["Value"]
            )
        )
    if "Detail" in data:
        out["detail"] = data["Detail"]
    return out
