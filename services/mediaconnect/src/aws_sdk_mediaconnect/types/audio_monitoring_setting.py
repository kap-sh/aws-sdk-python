"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AudioMonitoringSetting``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.silent_audio

class AudioMonitoringSetting(TypedDict):
    silent_audio: NotRequired["aws_sdk_mediaconnect.types.silent_audio.SilentAudio"]
    """<p> Detects periods of silence. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AudioMonitoringSetting) -> dict:
    out: dict = {}
    if "silent_audio" in value:
        import aws_sdk_mediaconnect.types.silent_audio
        out["silentAudio"] = aws_sdk_mediaconnect.types.silent_audio.serialize_json(value["silent_audio"])
    return out


def deserialize_json(data: dict) -> AudioMonitoringSetting:
    out: AudioMonitoringSetting = {}  # type: ignore[typeddict-item]
    if "silentAudio" in data:
        import aws_sdk_mediaconnect.types.silent_audio
        out["silent_audio"] = aws_sdk_mediaconnect.types.silent_audio.deserialize_json(data["silentAudio"])
    return out