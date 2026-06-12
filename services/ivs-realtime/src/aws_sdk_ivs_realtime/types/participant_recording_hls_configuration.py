"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantRecordingHlsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_recording_target_segment_duration_seconds


class ParticipantRecordingHlsConfiguration(TypedDict):
    target_segment_duration_seconds: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_recording_target_segment_duration_seconds.ParticipantRecordingTargetSegmentDurationSeconds"
    ]
    """<p>Defines the target duration for recorded segments generated when recording a stage participant. Segments may have durations longer than the specified value when needed to ensure each segment begins with a keyframe. Default: 6.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantRecordingHlsConfiguration) -> dict:
    out: dict = {}
    if "target_segment_duration_seconds" in value:
        out["targetSegmentDurationSeconds"] = value["target_segment_duration_seconds"]
    return out


def deserialize_json(data: dict) -> ParticipantRecordingHlsConfiguration:
    out: ParticipantRecordingHlsConfiguration = {}  # type: ignore[typeddict-item]
    if "targetSegmentDurationSeconds" in data:
        out["target_segment_duration_seconds"] = data["targetSegmentDurationSeconds"]
    return out
