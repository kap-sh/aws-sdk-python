"""Generated from Smithy shape ``com.amazonaws.connect#IntervalDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.interval_period
    import capo_connect.types.string


class IntervalDetails(TypedDict, closed=True):
    time_zone: NotRequired["capo_connect.types.string.String"]
    """<p>The timezone applied to requested metrics.</p>"""
    interval_period: NotRequired["capo_connect.types.interval_period.IntervalPeriod"]
    """<p> <code>IntervalPeriod</code>: An aggregated grouping applied to request metrics. Valid <code>IntervalPeriod</code> values are: <code>FIFTEEN_MIN</code> | <code>THIRTY_MIN</code> | <code>HOUR</code> | <code>DAY</code> | <code>WEEK</code> | <code>TOTAL</code>. </p> <p>For example, if <code>IntervalPeriod</code> is selected <code>THIRTY_MIN</code>, <code>StartTime</code> and <code>EndTime</code> differs by 1 day, then Connect Customer returns 48 results in the response. Each result is aggregated by the THIRTY_MIN period. By default Connect Customer aggregates results based on the <code>TOTAL</code> interval period. </p> <p>The following list describes restrictions on <code>StartTime</code> and <code>EndTime</code> based on what <code>IntervalPeriod</code> is requested. </p> <ul> <li> <p> <code>FIFTEEN_MIN</code>: The difference between <code>StartTime</code> and <code>EndTime</code> must be less than 3 days.</p> </li> <li> <p> <code>THIRTY_MIN</code>: The difference between <code>StartTime</code> and <code>EndTime</code> must be less than 3 days.</p> </li> <li> <p> <code>HOUR</code>: The difference between <code>StartTime</code> and <code>EndTime</code> must be less than 3 days.</p> </li> <li> <p> <code>DAY</code>: The difference between <code>StartTime</code> and <code>EndTime</code> must be less than 35 days.</p> </li> <li> <p> <code>WEEK</code>: The difference between <code>StartTime</code> and <code>EndTime</code> must be less than 35 days.</p> </li> <li> <p> <code>TOTAL</code>: The difference between <code>StartTime</code> and <code>EndTime</code> must be less than 35 days.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntervalDetails) -> dict:
    out: dict = {}
    if "time_zone" in value:
        out["TimeZone"] = value["time_zone"]
    if "interval_period" in value:
        import capo_connect.types.interval_period

        out["IntervalPeriod"] = capo_connect.types.interval_period.serialize_json(
            value["interval_period"]
        )
    return out


def deserialize_json(data: dict) -> IntervalDetails:
    out: IntervalDetails = {}  # type: ignore[typeddict-item]
    if "TimeZone" in data:
        out["time_zone"] = data["TimeZone"]
    if "IntervalPeriod" in data:
        import capo_connect.types.interval_period

        out["interval_period"] = capo_connect.types.interval_period.deserialize_json(
            data["IntervalPeriod"]
        )
    return out
