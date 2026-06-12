"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ChannelDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.channel_id
    import aws_sdk_chime_sdk_media_pipelines.types.participant_role


class ChannelDefinition(TypedDict):
    channel_id: "aws_sdk_chime_sdk_media_pipelines.types.channel_id.ChannelId"
    """<p>The channel ID.</p>"""
    participant_role: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.participant_role.ParticipantRole"
    ]
    """<p>Specifies whether the audio in a channel belongs to the <code>AGENT</code> or <code>CUSTOMER</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelDefinition) -> dict:
    out: dict = {}
    out["ChannelId"] = value.get("channel_id", 0)
    if "participant_role" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.participant_role

        out["ParticipantRole"] = (
            aws_sdk_chime_sdk_media_pipelines.types.participant_role.serialize_json(
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
        import aws_sdk_chime_sdk_media_pipelines.types.participant_role

        out["participant_role"] = (
            aws_sdk_chime_sdk_media_pipelines.types.participant_role.deserialize_json(
                data["ParticipantRole"]
            )
        )
    return out
