"""Generated from Smithy shape ``com.amazonaws.medialive#AudioPidSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max8191
    import capo_medialive.types.__list_of_audio_pid


class AudioPidSelection(TypedDict, closed=True):
    pid: NotRequired["capo_medialive.types.__integer_min0_max8191.__integerMin0Max8191"]
    """Selects a specific PID from within a source."""
    pids: NotRequired["capo_medialive.types.__list_of_audio_pid.__listOfAudioPid"]
    """Selects one or more unique PIDs from within a source. When using 'pids', you can specify per-PID audio pre-mixer settings."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioPidSelection) -> dict:
    out: dict = {}
    if "pid" in value:
        out["pid"] = value["pid"]
    if "pids" in value:
        import capo_medialive.types.__list_of_audio_pid

        out["pids"] = capo_medialive.types.__list_of_audio_pid.serialize_json(
            value["pids"]
        )
    return out


def deserialize_json(data: dict) -> AudioPidSelection:
    out: AudioPidSelection = {}  # type: ignore[typeddict-item]
    if "pid" in data:
        out["pid"] = data["pid"]
    if "pids" in data:
        import capo_medialive.types.__list_of_audio_pid

        out["pids"] = capo_medialive.types.__list_of_audio_pid.deserialize_json(
            data["pids"]
        )
    return out
