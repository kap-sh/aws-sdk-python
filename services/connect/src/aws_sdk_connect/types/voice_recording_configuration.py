"""Generated from Smithy shape ``com.amazonaws.connect#VoiceRecordingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.ivr_recording_track
    import aws_sdk_connect.types.voice_recording_track


class VoiceRecordingConfiguration(TypedDict, closed=True):
    voice_recording_track: NotRequired[
        "aws_sdk_connect.types.voice_recording_track.VoiceRecordingTrack"
    ]
    """<p>Identifies which track is being recorded.</p>"""
    ivr_recording_track: NotRequired[
        "aws_sdk_connect.types.ivr_recording_track.IvrRecordingTrack"
    ]
    """<p>Identifies which IVR track is being recorded.</p> <p>One and only one of the track configurations should be presented in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceRecordingConfiguration) -> dict:
    out: dict = {}
    if "voice_recording_track" in value:
        import aws_sdk_connect.types.voice_recording_track

        out["VoiceRecordingTrack"] = (
            aws_sdk_connect.types.voice_recording_track.serialize_json(
                value["voice_recording_track"]
            )
        )
    if "ivr_recording_track" in value:
        import aws_sdk_connect.types.ivr_recording_track

        out["IvrRecordingTrack"] = (
            aws_sdk_connect.types.ivr_recording_track.serialize_json(
                value["ivr_recording_track"]
            )
        )
    return out


def deserialize_json(data: dict) -> VoiceRecordingConfiguration:
    out: VoiceRecordingConfiguration = {}  # type: ignore[typeddict-item]
    if "VoiceRecordingTrack" in data:
        import aws_sdk_connect.types.voice_recording_track

        out["voice_recording_track"] = (
            aws_sdk_connect.types.voice_recording_track.deserialize_json(
                data["VoiceRecordingTrack"]
            )
        )
    if "IvrRecordingTrack" in data:
        import aws_sdk_connect.types.ivr_recording_track

        out["ivr_recording_track"] = (
            aws_sdk_connect.types.ivr_recording_track.deserialize_json(
                data["IvrRecordingTrack"]
            )
        )
    return out
