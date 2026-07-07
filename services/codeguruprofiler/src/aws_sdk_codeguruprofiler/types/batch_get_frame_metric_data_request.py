"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#BatchGetFrameMetricDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.aggregation_period
    import aws_sdk_codeguruprofiler.types.frame_metrics
    import aws_sdk_codeguruprofiler.types.period
    import aws_sdk_codeguruprofiler.types.profiling_group_name
    import aws_sdk_codeguruprofiler.types.timestamp


class BatchGetFrameMetricDataRequest(TypedDict, closed=True):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p> The name of the profiling group associated with the the frame metrics used to return the time series values. </p>"""
    start_time: NotRequired["aws_sdk_codeguruprofiler.types.timestamp.Timestamp"]
    """<p> The start time of the time period for the frame metrics used to return the time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    end_time: NotRequired["aws_sdk_codeguruprofiler.types.timestamp.Timestamp"]
    """<p> The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    period: NotRequired["aws_sdk_codeguruprofiler.types.period.Period"]
    """<p> The duration of the frame metrics used to return the time series values. Specify using the ISO 8601 format. The maximum period duration is one day (<code>PT24H</code> or <code>P1D</code>). </p>"""
    target_resolution: NotRequired[
        "aws_sdk_codeguruprofiler.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The requested resolution of time steps for the returned time series of values. If the requested target resolution is not available due to data not being retained we provide a best effort result by falling back to the most granular available resolution after the target resolution. There are 3 valid values. </p> <ul> <li> <p> <code>P1D</code> — 1 day </p> </li> <li> <p> <code>PT1H</code> — 1 hour </p> </li> <li> <p> <code>PT5M</code> — 5 minutes </p> </li> </ul>"""
    frame_metrics: NotRequired[
        "aws_sdk_codeguruprofiler.types.frame_metrics.FrameMetrics"
    ]
    """<p> The details of the metrics that are used to request a time series of values. The metric includes the name of the frame, the aggregation type to calculate the metric value for the frame, and the thread states to use to get the count for the metric value of the frame.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFrameMetricDataRequest) -> dict:
    out: dict = {}
    if "frame_metrics" in value:
        import aws_sdk_codeguruprofiler.types.frame_metrics

        out["frameMetrics"] = (
            aws_sdk_codeguruprofiler.types.frame_metrics.serialize_json(
                value["frame_metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetFrameMetricDataRequest:
    out: BatchGetFrameMetricDataRequest = {}  # type: ignore[typeddict-item]
    if "frameMetrics" in data:
        import aws_sdk_codeguruprofiler.types.frame_metrics

        out["frame_metrics"] = (
            aws_sdk_codeguruprofiler.types.frame_metrics.deserialize_json(
                data["frameMetrics"]
            )
        )
    return out
