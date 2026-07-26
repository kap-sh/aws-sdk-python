"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AudioMonitoringSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.silent_audio


class AudioMonitoringSetting(TypedDict, closed=True):
    silent_audio: NotRequired["capo_mediaconnect.types.silent_audio.SilentAudio"]
    """<p> Detects periods of silence. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioMonitoringSetting) -> dict:
    out: dict = {}
    if "silent_audio" in value:
        import capo_mediaconnect.types.silent_audio

        out["silentAudio"] = capo_mediaconnect.types.silent_audio.serialize_json(
            value["silent_audio"]
        )
    return out


def deserialize_json(data: dict) -> AudioMonitoringSetting:
    out: AudioMonitoringSetting = {}  # type: ignore[typeddict-item]
    if "silentAudio" in data:
        import capo_mediaconnect.types.silent_audio

        out["silent_audio"] = capo_mediaconnect.types.silent_audio.deserialize_json(
            data["silentAudio"]
        )
    return out
