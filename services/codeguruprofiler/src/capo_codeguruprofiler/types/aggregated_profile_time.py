"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AggregatedProfileTime``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.aggregation_period
    import capo_codeguruprofiler.types.timestamp


class AggregatedProfileTime(TypedDict, closed=True):
    start: NotRequired["capo_codeguruprofiler.types.timestamp.Timestamp"]
    """<p> The time that aggregation of posted agent profiles for a profiling group starts. The aggregation profile contains profiles posted by the agent starting at this time for an aggregation period specified by the <code>period</code> property of the <code>AggregatedProfileTime</code> object. </p> <p> Specify <code>start</code> using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    period: NotRequired[
        "capo_codeguruprofiler.types.aggregation_period.AggregationPeriod"
    ]
    """<p> The aggregation period. This indicates the period during which an aggregation profile collects posted agent profiles for a profiling group. Use one of three valid durations that are specified using the ISO 8601 format. </p> <ul> <li> <p> <code>P1D</code> — 1 day </p> </li> <li> <p> <code>PT1H</code> — 1 hour </p> </li> <li> <p> <code>PT5M</code> — 5 minutes </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedProfileTime) -> dict:
    out: dict = {}
    if "start" in value:
        import capo_codeguruprofiler.types.timestamp

        out["start"] = capo_codeguruprofiler.types.timestamp.serialize_json(
            value["start"]
        )
    if "period" in value:
        out["period"] = value["period"]
    return out


def deserialize_json(data: dict) -> AggregatedProfileTime:
    out: AggregatedProfileTime = {}  # type: ignore[typeddict-item]
    if "start" in data:
        import capo_codeguruprofiler.types.timestamp

        out["start"] = capo_codeguruprofiler.types.timestamp.deserialize_json(
            data["start"]
        )
    if "period" in data:
        out["period"] = data["period"]
    return out
