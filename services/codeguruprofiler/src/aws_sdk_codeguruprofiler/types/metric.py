"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Metric``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.metric_type
    import aws_sdk_codeguruprofiler.types.strings


class Metric(TypedDict):
    frame_name: "str"
    """<p> The name of the method that appears as a frame in any stack in a profile. </p>"""
    type: "aws_sdk_codeguruprofiler.types.metric_type.MetricType"
    """<p> A type that specifies how a metric for a frame is analyzed. The supported value <code>AggregatedRelativeTotalTime</code> is an aggregation of the metric value for one frame that is calculated across the occurences of all frames in a profile.</p>"""
    thread_states: "aws_sdk_codeguruprofiler.types.strings.Strings"
    """<p> The list of application runtime thread states that is used to calculate the metric value for the frame. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Metric) -> dict:
    out: dict = {}
    out["frameName"] = value["frame_name"]
    out["type"] = value["type"]
    import aws_sdk_codeguruprofiler.types.strings

    out["threadStates"] = aws_sdk_codeguruprofiler.types.strings.serialize_json(
        value["thread_states"]
    )
    return out


def deserialize_json(data: dict) -> Metric:
    out: Metric = {}  # type: ignore[typeddict-item]
    if "frameName" in data:
        out["frame_name"] = data["frameName"]
    else:
        raise DeserializationError("Metric.frame_name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("Metric.type required")
    if "threadStates" in data:
        import aws_sdk_codeguruprofiler.types.strings

        out["thread_states"] = aws_sdk_codeguruprofiler.types.strings.deserialize_json(
            data["threadStates"]
        )
    else:
        raise DeserializationError("Metric.thread_states required")
    return out
