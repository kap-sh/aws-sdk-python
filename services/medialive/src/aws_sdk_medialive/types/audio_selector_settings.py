"""Generated from Smithy shape ``com.amazonaws.medialive#AudioSelectorSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.audio_hls_rendition_selection
    import aws_sdk_medialive.types.audio_language_selection
    import aws_sdk_medialive.types.audio_pid_selection
    import aws_sdk_medialive.types.audio_track_selection


class AudioSelectorSettings(TypedDict):
    audio_hls_rendition_selection: NotRequired[
        "aws_sdk_medialive.types.audio_hls_rendition_selection.AudioHlsRenditionSelection"
    ]
    audio_language_selection: NotRequired[
        "aws_sdk_medialive.types.audio_language_selection.AudioLanguageSelection"
    ]
    audio_pid_selection: NotRequired[
        "aws_sdk_medialive.types.audio_pid_selection.AudioPidSelection"
    ]
    audio_track_selection: NotRequired[
        "aws_sdk_medialive.types.audio_track_selection.AudioTrackSelection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AudioSelectorSettings) -> dict:
    out: dict = {}
    if "audio_hls_rendition_selection" in value:
        import aws_sdk_medialive.types.audio_hls_rendition_selection

        out["audioHlsRenditionSelection"] = (
            aws_sdk_medialive.types.audio_hls_rendition_selection.serialize_json(
                value["audio_hls_rendition_selection"]
            )
        )
    if "audio_language_selection" in value:
        import aws_sdk_medialive.types.audio_language_selection

        out["audioLanguageSelection"] = (
            aws_sdk_medialive.types.audio_language_selection.serialize_json(
                value["audio_language_selection"]
            )
        )
    if "audio_pid_selection" in value:
        import aws_sdk_medialive.types.audio_pid_selection

        out["audioPidSelection"] = (
            aws_sdk_medialive.types.audio_pid_selection.serialize_json(
                value["audio_pid_selection"]
            )
        )
    if "audio_track_selection" in value:
        import aws_sdk_medialive.types.audio_track_selection

        out["audioTrackSelection"] = (
            aws_sdk_medialive.types.audio_track_selection.serialize_json(
                value["audio_track_selection"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioSelectorSettings:
    out: AudioSelectorSettings = {}  # type: ignore[typeddict-item]
    if "audioHlsRenditionSelection" in data:
        import aws_sdk_medialive.types.audio_hls_rendition_selection

        out["audio_hls_rendition_selection"] = (
            aws_sdk_medialive.types.audio_hls_rendition_selection.deserialize_json(
                data["audioHlsRenditionSelection"]
            )
        )
    if "audioLanguageSelection" in data:
        import aws_sdk_medialive.types.audio_language_selection

        out["audio_language_selection"] = (
            aws_sdk_medialive.types.audio_language_selection.deserialize_json(
                data["audioLanguageSelection"]
            )
        )
    if "audioPidSelection" in data:
        import aws_sdk_medialive.types.audio_pid_selection

        out["audio_pid_selection"] = (
            aws_sdk_medialive.types.audio_pid_selection.deserialize_json(
                data["audioPidSelection"]
            )
        )
    if "audioTrackSelection" in data:
        import aws_sdk_medialive.types.audio_track_selection

        out["audio_track_selection"] = (
            aws_sdk_medialive.types.audio_track_selection.deserialize_json(
                data["audioTrackSelection"]
            )
        )
    return out
