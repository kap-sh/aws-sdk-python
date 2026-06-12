"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#BatchGetFrameMetricDataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.aggregation_period
    import aws_sdk_codeguruprofiler.types.frame_metric_data
    import aws_sdk_codeguruprofiler.types.list_of_timestamps
    import aws_sdk_codeguruprofiler.types.timestamp
    import aws_sdk_codeguruprofiler.types.unprocessed_end_time_map


class BatchGetFrameMetricDataResponse(TypedDict):
    start_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The start time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    end_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    resolution: "aws_sdk_codeguruprofiler.types.aggregation_period.AggregationPeriod"
    """<p>Resolution or granularity of the profile data used to generate the time series. This is the value used to jump through time steps in a time series. There are 3 valid values. </p> <ul> <li> <p> <code>P1D</code> — 1 day </p> </li> <li> <p> <code>PT1H</code> — 1 hour </p> </li> <li> <p> <code>PT5M</code> — 5 minutes </p> </li> </ul>"""
    end_times: "aws_sdk_codeguruprofiler.types.list_of_timestamps.ListOfTimestamps"
    """<p> List of instances, or time steps, in the time series. For example, if the <code>period</code> is one day (<code>PT24H)</code>), and the <code>resolution</code> is five minutes (<code>PT5M</code>), then there are 288 <code>endTimes</code> in the list that are each five minutes appart. </p>"""
    unprocessed_end_times: (
        "aws_sdk_codeguruprofiler.types.unprocessed_end_time_map.UnprocessedEndTimeMap"
    )
    """<p>List of instances which remained unprocessed. This will create a missing time step in the list of end times.</p>"""
    frame_metric_data: (
        "aws_sdk_codeguruprofiler.types.frame_metric_data.FrameMetricData"
    )
    """<p>Details of the metrics to request a time series of values. The metric includes the name of the frame, the aggregation type to calculate the metric value for the frame, and the thread states to use to get the count for the metric value of the frame.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFrameMetricDataResponse) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.timestamp

    out["startTime"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_codeguruprofiler.types.timestamp

    out["endTime"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
        value["end_time"]
    )
    out["resolution"] = value["resolution"]
    import aws_sdk_codeguruprofiler.types.list_of_timestamps

    out["endTimes"] = aws_sdk_codeguruprofiler.types.list_of_timestamps.serialize_json(
        value["end_times"]
    )
    import aws_sdk_codeguruprofiler.types.unprocessed_end_time_map

    out["unprocessedEndTimes"] = (
        aws_sdk_codeguruprofiler.types.unprocessed_end_time_map.serialize_json(
            value["unprocessed_end_times"]
        )
    )
    import aws_sdk_codeguruprofiler.types.frame_metric_data

    out["frameMetricData"] = (
        aws_sdk_codeguruprofiler.types.frame_metric_data.serialize_json(
            value["frame_metric_data"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetFrameMetricDataResponse:
    out: BatchGetFrameMetricDataResponse = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["start_time"] = aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError(
            "BatchGetFrameMetricDataResponse.start_time required"
        )
    if "endTime" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["end_time"] = aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("BatchGetFrameMetricDataResponse.end_time required")
    if "resolution" in data:
        out["resolution"] = data["resolution"]
    else:
        raise DeserializationError(
            "BatchGetFrameMetricDataResponse.resolution required"
        )
    if "endTimes" in data:
        import aws_sdk_codeguruprofiler.types.list_of_timestamps

        out["end_times"] = (
            aws_sdk_codeguruprofiler.types.list_of_timestamps.deserialize_json(
                data["endTimes"]
            )
        )
    else:
        raise DeserializationError("BatchGetFrameMetricDataResponse.end_times required")
    if "unprocessedEndTimes" in data:
        import aws_sdk_codeguruprofiler.types.unprocessed_end_time_map

        out["unprocessed_end_times"] = (
            aws_sdk_codeguruprofiler.types.unprocessed_end_time_map.deserialize_json(
                data["unprocessedEndTimes"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetFrameMetricDataResponse.unprocessed_end_times required"
        )
    if "frameMetricData" in data:
        import aws_sdk_codeguruprofiler.types.frame_metric_data

        out["frame_metric_data"] = (
            aws_sdk_codeguruprofiler.types.frame_metric_data.deserialize_json(
                data["frameMetricData"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetFrameMetricDataResponse.frame_metric_data required"
        )
    return out
