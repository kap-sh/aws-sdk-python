"""Generated from Smithy shape ``com.amazonaws.xray#TimeSeriesServiceStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.edge_statistics
    import capo_xray.types.forecast_statistics
    import capo_xray.types.histogram
    import capo_xray.types.service_statistics
    import capo_xray.types.timestamp


class TimeSeriesServiceStatistics(TypedDict, closed=True):
    timestamp: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>Timestamp of the window for which statistics are aggregated.</p>"""
    edge_summary_statistics: NotRequired[
        "capo_xray.types.edge_statistics.EdgeStatistics"
    ]
    service_summary_statistics: NotRequired[
        "capo_xray.types.service_statistics.ServiceStatistics"
    ]
    service_forecast_statistics: NotRequired[
        "capo_xray.types.forecast_statistics.ForecastStatistics"
    ]
    """<p>The forecasted high and low fault count values.</p>"""
    response_time_histogram: NotRequired["capo_xray.types.histogram.Histogram"]
    """<p>The response time histogram for the selected entities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesServiceStatistics) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_xray.types.timestamp

        out["Timestamp"] = capo_xray.types.timestamp.serialize_json(value["timestamp"])
    if "edge_summary_statistics" in value:
        import capo_xray.types.edge_statistics

        out["EdgeSummaryStatistics"] = capo_xray.types.edge_statistics.serialize_json(
            value["edge_summary_statistics"]
        )
    if "service_summary_statistics" in value:
        import capo_xray.types.service_statistics

        out["ServiceSummaryStatistics"] = (
            capo_xray.types.service_statistics.serialize_json(
                value["service_summary_statistics"]
            )
        )
    if "service_forecast_statistics" in value:
        import capo_xray.types.forecast_statistics

        out["ServiceForecastStatistics"] = (
            capo_xray.types.forecast_statistics.serialize_json(
                value["service_forecast_statistics"]
            )
        )
    if "response_time_histogram" in value:
        import capo_xray.types.histogram

        out["ResponseTimeHistogram"] = capo_xray.types.histogram.serialize_json(
            value["response_time_histogram"]
        )
    return out


def deserialize_json(data: dict) -> TimeSeriesServiceStatistics:
    out: TimeSeriesServiceStatistics = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import capo_xray.types.timestamp

        out["timestamp"] = capo_xray.types.timestamp.deserialize_json(data["Timestamp"])
    if "EdgeSummaryStatistics" in data:
        import capo_xray.types.edge_statistics

        out["edge_summary_statistics"] = (
            capo_xray.types.edge_statistics.deserialize_json(
                data["EdgeSummaryStatistics"]
            )
        )
    if "ServiceSummaryStatistics" in data:
        import capo_xray.types.service_statistics

        out["service_summary_statistics"] = (
            capo_xray.types.service_statistics.deserialize_json(
                data["ServiceSummaryStatistics"]
            )
        )
    if "ServiceForecastStatistics" in data:
        import capo_xray.types.forecast_statistics

        out["service_forecast_statistics"] = (
            capo_xray.types.forecast_statistics.deserialize_json(
                data["ServiceForecastStatistics"]
            )
        )
    if "ResponseTimeHistogram" in data:
        import capo_xray.types.histogram

        out["response_time_histogram"] = capo_xray.types.histogram.deserialize_json(
            data["ResponseTimeHistogram"]
        )
    return out
