"""Generated from Smithy shape ``com.amazonaws.iot#ListFleetMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.fleet_metric_name_and_arn_list
    import capo_iot.types.next_token


class ListFleetMetricsResponse(TypedDict, closed=True):
    fleet_metrics: NotRequired[
        "capo_iot.types.fleet_metric_name_and_arn_list.FleetMetricNameAndArnList"
    ]
    """<p>The list of fleet metrics objects.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results. Will not be returned if the operation has returned all results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFleetMetricsResponse) -> dict:
    out: dict = {}
    if "fleet_metrics" in value:
        import capo_iot.types.fleet_metric_name_and_arn_list

        out["fleetMetrics"] = (
            capo_iot.types.fleet_metric_name_and_arn_list.serialize_json(
                value["fleet_metrics"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFleetMetricsResponse:
    out: ListFleetMetricsResponse = {}  # type: ignore[typeddict-item]
    if "fleetMetrics" in data:
        import capo_iot.types.fleet_metric_name_and_arn_list

        out["fleet_metrics"] = (
            capo_iot.types.fleet_metric_name_and_arn_list.deserialize_json(
                data["fleetMetrics"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
