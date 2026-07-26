"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Timing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.nullable_long


class Timing(TypedDict, closed=True):
    submit_time_millis: NotRequired[
        "capo_elastic_transcoder.types.nullable_long.NullableLong"
    ]
    """<p>The time the job was submitted to Elastic Transcoder, in epoch milliseconds.</p>"""
    start_time_millis: NotRequired[
        "capo_elastic_transcoder.types.nullable_long.NullableLong"
    ]
    """<p>The time the job began transcoding, in epoch milliseconds.</p>"""
    finish_time_millis: NotRequired[
        "capo_elastic_transcoder.types.nullable_long.NullableLong"
    ]
    """<p>The time the job finished transcoding, in epoch milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Timing) -> dict:
    out: dict = {}
    if "submit_time_millis" in value:
        out["SubmitTimeMillis"] = value["submit_time_millis"]
    if "start_time_millis" in value:
        out["StartTimeMillis"] = value["start_time_millis"]
    if "finish_time_millis" in value:
        out["FinishTimeMillis"] = value["finish_time_millis"]
    return out


def deserialize_json(data: dict) -> Timing:
    out: Timing = {}  # type: ignore[typeddict-item]
    if "SubmitTimeMillis" in data:
        out["submit_time_millis"] = data["SubmitTimeMillis"]
    if "StartTimeMillis" in data:
        out["start_time_millis"] = data["StartTimeMillis"]
    if "FinishTimeMillis" in data:
        out["finish_time_millis"] = data["FinishTimeMillis"]
    return out
