"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetChannelMessageStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_message_status_structure


class GetChannelMessageStatusResponse(TypedDict):
    status: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_message_status_structure.ChannelMessageStatusStructure"
    ]
    """<p>The message status and details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelMessageStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_message_status_structure

        out["Status"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_status_structure.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetChannelMessageStatusResponse:
    out: GetChannelMessageStatusResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_message_status_structure

        out["status"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_status_structure.deserialize_json(
                data["Status"]
            )
        )
    return out
