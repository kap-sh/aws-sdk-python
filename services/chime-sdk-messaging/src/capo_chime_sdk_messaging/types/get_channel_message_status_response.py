"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetChannelMessageStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_message_status_structure


class GetChannelMessageStatusResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_chime_sdk_messaging.types.channel_message_status_structure.ChannelMessageStatusStructure"
    ]
    """<p>The message status and details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelMessageStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_chime_sdk_messaging.types.channel_message_status_structure

        out["Status"] = (
            capo_chime_sdk_messaging.types.channel_message_status_structure.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetChannelMessageStatusResponse:
    out: GetChannelMessageStatusResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_chime_sdk_messaging.types.channel_message_status_structure

        out["status"] = (
            capo_chime_sdk_messaging.types.channel_message_status_structure.deserialize_json(
                data["Status"]
            )
        )
    return out
