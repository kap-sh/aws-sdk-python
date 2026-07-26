"""Generated from Smithy shape ``com.amazonaws.connect#MetricInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.interval_period
    import capo_connect.types.timestamp


class MetricInterval(TypedDict, closed=True):
    interval: NotRequired["capo_connect.types.interval_period.IntervalPeriod"]
    """<p>The interval period provided in the API request. </p>"""
    start_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp, in UNIX Epoch time format. Start time is based on the interval period selected. </p>"""
    end_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp, in UNIX Epoch time format. End time is based on the interval period selected. For example, If <code>IntervalPeriod</code> is selected <code>THIRTY_MIN</code>, <code>StartTime</code> and <code>EndTime</code> in the API request differs by 1 day, then 48 results are returned in the response. Each result is aggregated by the 30 minutes period, with each <code>StartTime</code> and <code>EndTime</code> differing by 30 minutes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricInterval) -> dict:
    out: dict = {}
    if "interval" in value:
        import capo_connect.types.interval_period

        out["Interval"] = capo_connect.types.interval_period.serialize_json(
            value["interval"]
        )
    if "start_time" in value:
        import capo_connect.types.timestamp

        out["StartTime"] = capo_connect.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_connect.types.timestamp

        out["EndTime"] = capo_connect.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> MetricInterval:
    out: MetricInterval = {}  # type: ignore[typeddict-item]
    if "Interval" in data:
        import capo_connect.types.interval_period

        out["interval"] = capo_connect.types.interval_period.deserialize_json(
            data["Interval"]
        )
    if "StartTime" in data:
        import capo_connect.types.timestamp

        out["start_time"] = capo_connect.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_connect.types.timestamp

        out["end_time"] = capo_connect.types.timestamp.deserialize_json(data["EndTime"])
    return out
