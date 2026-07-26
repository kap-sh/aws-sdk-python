"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessageStatusStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_message_status
    import capo_chime_sdk_messaging.types.status_detail


class ChannelMessageStatusStructure(TypedDict, closed=True):
    value: NotRequired[
        "capo_chime_sdk_messaging.types.channel_message_status.ChannelMessageStatus"
    ]
    """<p>The message status value.</p>"""
    detail: NotRequired["capo_chime_sdk_messaging.types.status_detail.StatusDetail"]
    """<p>Contains more details about the message status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessageStatusStructure) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_chime_sdk_messaging.types.channel_message_status

        out["Value"] = (
            capo_chime_sdk_messaging.types.channel_message_status.serialize_json(
                value["value"]
            )
        )
    if "detail" in value:
        out["Detail"] = value["detail"]
    return out


def deserialize_json(data: dict) -> ChannelMessageStatusStructure:
    out: ChannelMessageStatusStructure = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        import capo_chime_sdk_messaging.types.channel_message_status

        out["value"] = (
            capo_chime_sdk_messaging.types.channel_message_status.deserialize_json(
                data["Value"]
            )
        )
    if "Detail" in data:
        out["detail"] = data["Detail"]
    return out
