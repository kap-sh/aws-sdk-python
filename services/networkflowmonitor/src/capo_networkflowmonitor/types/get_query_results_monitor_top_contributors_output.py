"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryResultsMonitorTopContributorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.metric_unit
    import capo_networkflowmonitor.types.monitor_top_contributors_row_list


class GetQueryResultsMonitorTopContributorsOutput(TypedDict, closed=True):
    unit: NotRequired["capo_networkflowmonitor.types.metric_unit.MetricUnit"]
    """<p>The units for a metric returned by the query.</p>"""
    top_contributors: NotRequired[
        "capo_networkflowmonitor.types.monitor_top_contributors_row_list.MonitorTopContributorsRowList"
    ]
    """<p>The top contributor network flows overall for a specific metric type, for example, the number of retransmissions.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryResultsMonitorTopContributorsOutput) -> dict:
    out: dict = {}
    if "unit" in value:
        import capo_networkflowmonitor.types.metric_unit

        out["unit"] = capo_networkflowmonitor.types.metric_unit.serialize_json(
            value["unit"]
        )
    if "top_contributors" in value:
        import capo_networkflowmonitor.types.monitor_top_contributors_row_list

        out["topContributors"] = (
            capo_networkflowmonitor.types.monitor_top_contributors_row_list.serialize_json(
                value["top_contributors"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetQueryResultsMonitorTopContributorsOutput:
    out: GetQueryResultsMonitorTopContributorsOutput = {}  # type: ignore[typeddict-item]
    if "unit" in data:
        import capo_networkflowmonitor.types.metric_unit

        out["unit"] = capo_networkflowmonitor.types.metric_unit.deserialize_json(
            data["unit"]
        )
    if "topContributors" in data:
        import capo_networkflowmonitor.types.monitor_top_contributors_row_list

        out["top_contributors"] = (
            capo_networkflowmonitor.types.monitor_top_contributors_row_list.deserialize_json(
                data["topContributors"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
