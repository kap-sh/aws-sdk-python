"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CompositionRecordingHlsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.composition_recording_target_segment_duration_seconds


class CompositionRecordingHlsConfiguration(TypedDict, closed=True):
    target_segment_duration_seconds: NotRequired[
        "capo_ivs_realtime.types.composition_recording_target_segment_duration_seconds.CompositionRecordingTargetSegmentDurationSeconds"
    ]
    """<p>Defines the target duration for recorded segments generated when using composite recording. Default: 2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositionRecordingHlsConfiguration) -> dict:
    out: dict = {}
    if "target_segment_duration_seconds" in value:
        out["targetSegmentDurationSeconds"] = value["target_segment_duration_seconds"]
    return out


def deserialize_json(data: dict) -> CompositionRecordingHlsConfiguration:
    out: CompositionRecordingHlsConfiguration = {}  # type: ignore[typeddict-item]
    if "targetSegmentDurationSeconds" in data:
        out["target_segment_duration_seconds"] = data["targetSegmentDurationSeconds"]
    return out
