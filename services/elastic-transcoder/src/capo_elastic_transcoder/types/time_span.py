"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#TimeSpan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.time


class TimeSpan(TypedDict, closed=True):
    start_time: NotRequired["capo_elastic_transcoder.types.time.Time"]
    """<p>The place in the input file where you want a clip to start. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you don't specify a value, Elastic Transcoder starts at the beginning of the input file.</p>"""
    duration: NotRequired["capo_elastic_transcoder.types.time.Time"]
    """<p>The duration of the clip. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you don't specify a value, Elastic Transcoder creates an output file from StartTime to the end of the file.</p> <p>If you specify a value longer than the duration of the input file, Elastic Transcoder transcodes the file and returns a warning message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeSpan) -> dict:
    out: dict = {}
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> TimeSpan:
    out: TimeSpan = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    return out
