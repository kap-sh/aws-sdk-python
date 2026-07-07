"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ChannelDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transcribe_streaming.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.channel_id
    import aws_sdk_transcribe_streaming.types.participant_role


class ChannelDefinition(TypedDict, closed=True):
    channel_id: "aws_sdk_transcribe_streaming.types.channel_id.ChannelId"
    """<p>Specify the audio channel you want to define.</p>"""
    participant_role: (
        "aws_sdk_transcribe_streaming.types.participant_role.ParticipantRole"
    )
    """<p>Specify the speaker you want to define. Omitting this parameter is equivalent to specifying both participants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelDefinition) -> dict:
    out: dict = {}
    out["ChannelId"] = value.get("channel_id", 0)
    import aws_sdk_transcribe_streaming.types.participant_role

    out["ParticipantRole"] = (
        aws_sdk_transcribe_streaming.types.participant_role.serialize_json(
            value["participant_role"]
        )
    )
    return out


def deserialize_json(data: dict) -> ChannelDefinition:
    out: ChannelDefinition = {}  # type: ignore[typeddict-item]
    if "ChannelId" in data:
        out["channel_id"] = data["ChannelId"]
    else:
        out["channel_id"] = 0
    if "ParticipantRole" in data:
        import aws_sdk_transcribe_streaming.types.participant_role

        out["participant_role"] = (
            aws_sdk_transcribe_streaming.types.participant_role.deserialize_json(
                data["ParticipantRole"]
            )
        )
    else:
        raise DeserializationError("ChannelDefinition.participant_role required")
    return out
