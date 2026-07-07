"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35SpliceInsertScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__long_min0_max4294967295
    import aws_sdk_medialive.types.__long_min0_max8589934591


class Scte35SpliceInsertScheduleActionSettings(TypedDict, closed=True):
    duration: NotRequired[
        "aws_sdk_medialive.types.__long_min0_max8589934591.__longMin0Max8589934591"
    ]
    """Optional, the duration for the splice_insert, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. If you enter a duration, there is an expectation that the downstream system can read the duration and cue in at that time. If you do not enter a duration, the splice_insert will continue indefinitely and there is an expectation that you will enter a return_to_network to end the splice_insert at the appropriate time."""
    splice_event_id: NotRequired[
        "aws_sdk_medialive.types.__long_min0_max4294967295.__longMin0Max4294967295"
    ]
    """The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte35SpliceInsertScheduleActionSettings) -> dict:
    out: dict = {}
    if "duration" in value:
        out["duration"] = value["duration"]
    if "splice_event_id" in value:
        out["spliceEventId"] = value["splice_event_id"]
    return out


def deserialize_json(data: dict) -> Scte35SpliceInsertScheduleActionSettings:
    out: Scte35SpliceInsertScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "spliceEventId" in data:
        out["splice_event_id"] = data["spliceEventId"]
    return out
