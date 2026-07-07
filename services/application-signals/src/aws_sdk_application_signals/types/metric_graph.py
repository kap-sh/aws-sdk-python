"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricGraph``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.metric_data_queries


class MetricGraph(TypedDict, closed=True):
    metric_data_queries: NotRequired[
        "aws_sdk_application_signals.types.metric_data_queries.MetricDataQueries"
    ]
    """<p>An array of metric data queries that define the metrics to be retrieved and analyzed as part of the audit finding context.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time for the metric data included in this graph. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time for the metric data included in this graph. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricGraph) -> dict:
    out: dict = {}
    if "metric_data_queries" in value:
        import aws_sdk_application_signals.types.metric_data_queries

        out["MetricDataQueries"] = (
            aws_sdk_application_signals.types.metric_data_queries.serialize_json(
                value["metric_data_queries"]
            )
        )
    if "start_time" in value:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["StartTime"] = (
            aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["EndTime"] = (
            aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetricGraph:
    out: MetricGraph = {}  # type: ignore[typeddict-item]
    if "MetricDataQueries" in data:
        import aws_sdk_application_signals.types.metric_data_queries

        out["metric_data_queries"] = (
            aws_sdk_application_signals.types.metric_data_queries.deserialize_json(
                data["MetricDataQueries"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    return out
