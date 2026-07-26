"""Generated from Smithy shape ``com.amazonaws.costexplorer#UtilizationByTime``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.reservation_aggregates
    import capo_cost_explorer.types.reservation_utilization_groups


class UtilizationByTime(TypedDict, closed=True):
    time_period: NotRequired["capo_cost_explorer.types.date_interval.DateInterval"]
    """<p>The period of time that this utilization was used for.</p>"""
    groups: NotRequired[
        "capo_cost_explorer.types.reservation_utilization_groups.ReservationUtilizationGroups"
    ]
    """<p>The groups that this utilization result uses.</p>"""
    total: NotRequired[
        "capo_cost_explorer.types.reservation_aggregates.ReservationAggregates"
    ]
    """<p>The total number of reservation hours that were used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UtilizationByTime) -> dict:
    out: dict = {}
    if "time_period" in value:
        import capo_cost_explorer.types.date_interval

        out["TimePeriod"] = (
            capo_cost_explorer.types.date_interval.serialize_aws_json_1_1(
                value["time_period"]
            )
        )
    if "groups" in value:
        import capo_cost_explorer.types.reservation_utilization_groups

        out["Groups"] = (
            capo_cost_explorer.types.reservation_utilization_groups.serialize_aws_json_1_1(
                value["groups"]
            )
        )
    if "total" in value:
        import capo_cost_explorer.types.reservation_aggregates

        out["Total"] = (
            capo_cost_explorer.types.reservation_aggregates.serialize_aws_json_1_1(
                value["total"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UtilizationByTime:
    out: UtilizationByTime = {}  # type: ignore[typeddict-item]
    if "TimePeriod" in data:
        import capo_cost_explorer.types.date_interval

        out["time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    if "Groups" in data:
        import capo_cost_explorer.types.reservation_utilization_groups

        out["groups"] = (
            capo_cost_explorer.types.reservation_utilization_groups.deserialize_aws_json_1_1(
                data["Groups"]
            )
        )
    if "Total" in data:
        import capo_cost_explorer.types.reservation_aggregates

        out["total"] = (
            capo_cost_explorer.types.reservation_aggregates.deserialize_aws_json_1_1(
                data["Total"]
            )
        )
    return out
