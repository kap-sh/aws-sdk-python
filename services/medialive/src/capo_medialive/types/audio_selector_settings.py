"""Generated from Smithy shape ``com.amazonaws.medialive#AudioSelectorSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.audio_hls_rendition_selection
    import capo_medialive.types.audio_language_selection
    import capo_medialive.types.audio_pid_selection
    import capo_medialive.types.audio_track_selection


class AudioSelectorSettings(TypedDict, closed=True):
    audio_hls_rendition_selection: NotRequired[
        "capo_medialive.types.audio_hls_rendition_selection.AudioHlsRenditionSelection"
    ]
    audio_language_selection: NotRequired[
        "capo_medialive.types.audio_language_selection.AudioLanguageSelection"
    ]
    audio_pid_selection: NotRequired[
        "capo_medialive.types.audio_pid_selection.AudioPidSelection"
    ]
    audio_track_selection: NotRequired[
        "capo_medialive.types.audio_track_selection.AudioTrackSelection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AudioSelectorSettings) -> dict:
    out: dict = {}
    if "audio_hls_rendition_selection" in value:
        import capo_medialive.types.audio_hls_rendition_selection

        out["audioHlsRenditionSelection"] = (
            capo_medialive.types.audio_hls_rendition_selection.serialize_json(
                value["audio_hls_rendition_selection"]
            )
        )
    if "audio_language_selection" in value:
        import capo_medialive.types.audio_language_selection

        out["audioLanguageSelection"] = (
            capo_medialive.types.audio_language_selection.serialize_json(
                value["audio_language_selection"]
            )
        )
    if "audio_pid_selection" in value:
        import capo_medialive.types.audio_pid_selection

        out["audioPidSelection"] = (
            capo_medialive.types.audio_pid_selection.serialize_json(
                value["audio_pid_selection"]
            )
        )
    if "audio_track_selection" in value:
        import capo_medialive.types.audio_track_selection

        out["audioTrackSelection"] = (
            capo_medialive.types.audio_track_selection.serialize_json(
                value["audio_track_selection"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioSelectorSettings:
    out: AudioSelectorSettings = {}  # type: ignore[typeddict-item]
    if "audioHlsRenditionSelection" in data:
        import capo_medialive.types.audio_hls_rendition_selection

        out["audio_hls_rendition_selection"] = (
            capo_medialive.types.audio_hls_rendition_selection.deserialize_json(
                data["audioHlsRenditionSelection"]
            )
        )
    if "audioLanguageSelection" in data:
        import capo_medialive.types.audio_language_selection

        out["audio_language_selection"] = (
            capo_medialive.types.audio_language_selection.deserialize_json(
                data["audioLanguageSelection"]
            )
        )
    if "audioPidSelection" in data:
        import capo_medialive.types.audio_pid_selection

        out["audio_pid_selection"] = (
            capo_medialive.types.audio_pid_selection.deserialize_json(
                data["audioPidSelection"]
            )
        )
    if "audioTrackSelection" in data:
        import capo_medialive.types.audio_track_selection

        out["audio_track_selection"] = (
            capo_medialive.types.audio_track_selection.deserialize_json(
                data["audioTrackSelection"]
            )
        )
    return out
