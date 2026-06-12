"""Generated from Smithy shape ``com.amazonaws.xray#TimeSeriesServiceStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.edge_statistics
    import aws_sdk_xray.types.forecast_statistics
    import aws_sdk_xray.types.histogram
    import aws_sdk_xray.types.service_statistics
    import aws_sdk_xray.types.timestamp


class TimeSeriesServiceStatistics(TypedDict):
    timestamp: NotRequired["aws_sdk_xray.types.timestamp.Timestamp"]
    """<p>Timestamp of the window for which statistics are aggregated.</p>"""
    edge_summary_statistics: NotRequired[
        "aws_sdk_xray.types.edge_statistics.EdgeStatistics"
    ]
    service_summary_statistics: NotRequired[
        "aws_sdk_xray.types.service_statistics.ServiceStatistics"
    ]
    service_forecast_statistics: NotRequired[
        "aws_sdk_xray.types.forecast_statistics.ForecastStatistics"
    ]
    """<p>The forecasted high and low fault count values.</p>"""
    response_time_histogram: NotRequired["aws_sdk_xray.types.histogram.Histogram"]
    """<p>The response time histogram for the selected entities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesServiceStatistics) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_xray.types.timestamp

        out["Timestamp"] = aws_sdk_xray.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "edge_summary_statistics" in value:
        import aws_sdk_xray.types.edge_statistics

        out["EdgeSummaryStatistics"] = (
            aws_sdk_xray.types.edge_statistics.serialize_json(
                value["edge_summary_statistics"]
            )
        )
    if "service_summary_statistics" in value:
        import aws_sdk_xray.types.service_statistics

        out["ServiceSummaryStatistics"] = (
            aws_sdk_xray.types.service_statistics.serialize_json(
                value["service_summary_statistics"]
            )
        )
    if "service_forecast_statistics" in value:
        import aws_sdk_xray.types.forecast_statistics

        out["ServiceForecastStatistics"] = (
            aws_sdk_xray.types.forecast_statistics.serialize_json(
                value["service_forecast_statistics"]
            )
        )
    if "response_time_histogram" in value:
        import aws_sdk_xray.types.histogram

        out["ResponseTimeHistogram"] = aws_sdk_xray.types.histogram.serialize_json(
            value["response_time_histogram"]
        )
    return out


def deserialize_json(data: dict) -> TimeSeriesServiceStatistics:
    out: TimeSeriesServiceStatistics = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_xray.types.timestamp

        out["timestamp"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    if "EdgeSummaryStatistics" in data:
        import aws_sdk_xray.types.edge_statistics

        out["edge_summary_statistics"] = (
            aws_sdk_xray.types.edge_statistics.deserialize_json(
                data["EdgeSummaryStatistics"]
            )
        )
    if "ServiceSummaryStatistics" in data:
        import aws_sdk_xray.types.service_statistics

        out["service_summary_statistics"] = (
            aws_sdk_xray.types.service_statistics.deserialize_json(
                data["ServiceSummaryStatistics"]
            )
        )
    if "ServiceForecastStatistics" in data:
        import aws_sdk_xray.types.forecast_statistics

        out["service_forecast_statistics"] = (
            aws_sdk_xray.types.forecast_statistics.deserialize_json(
                data["ServiceForecastStatistics"]
            )
        )
    if "ResponseTimeHistogram" in data:
        import aws_sdk_xray.types.histogram

        out["response_time_histogram"] = aws_sdk_xray.types.histogram.deserialize_json(
            data["ResponseTimeHistogram"]
        )
    return out
