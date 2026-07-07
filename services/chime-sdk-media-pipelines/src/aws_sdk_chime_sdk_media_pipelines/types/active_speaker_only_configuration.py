"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ActiveSpeakerOnlyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.active_speaker_position


class ActiveSpeakerOnlyConfiguration(TypedDict, closed=True):
    active_speaker_position: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.active_speaker_position.ActiveSpeakerPosition"
    ]
    """<p>The position of the <code>ActiveSpeakerOnly</code> video tile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveSpeakerOnlyConfiguration) -> dict:
    out: dict = {}
    if "active_speaker_position" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.active_speaker_position

        out["ActiveSpeakerPosition"] = (
            aws_sdk_chime_sdk_media_pipelines.types.active_speaker_position.serialize_json(
                value["active_speaker_position"]
            )
        )
    return out


def deserialize_json(data: dict) -> ActiveSpeakerOnlyConfiguration:
    out: ActiveSpeakerOnlyConfiguration = {}  # type: ignore[typeddict-item]
    if "ActiveSpeakerPosition" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.active_speaker_position

        out["active_speaker_position"] = (
            aws_sdk_chime_sdk_media_pipelines.types.active_speaker_position.deserialize_json(
                data["ActiveSpeakerPosition"]
            )
        )
    return out
