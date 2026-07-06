"""Generated from Smithy shape ``com.amazonaws.transcribe#ChannelDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.channel_id
    import aws_sdk_transcribe.types.participant_role


class ChannelDefinition(TypedDict, closed=True):
    channel_id: "aws_sdk_transcribe.types.channel_id.ChannelId"
    """<p>Specify the audio channel you want to define.</p>"""
    participant_role: NotRequired[
        "aws_sdk_transcribe.types.participant_role.ParticipantRole"
    ]
    """<p>Specify the speaker you want to define. Omitting this parameter is equivalent to specifying both participants.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelDefinition) -> dict:
    out: dict = {}
    out["ChannelId"] = value.get("channel_id", 0)
    if "participant_role" in value:
        import aws_sdk_transcribe.types.participant_role

        out["ParticipantRole"] = (
            aws_sdk_transcribe.types.participant_role.serialize_aws_json_1_1(
                value["participant_role"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelDefinition:
    out: ChannelDefinition = {}  # type: ignore[typeddict-item]
    if "ChannelId" in data:
        out["channel_id"] = data["ChannelId"]
    else:
        out["channel_id"] = 0
    if "ParticipantRole" in data:
        import aws_sdk_transcribe.types.participant_role

        out["participant_role"] = (
            aws_sdk_transcribe.types.participant_role.deserialize_aws_json_1_1(
                data["ParticipantRole"]
            )
        )
    return out
