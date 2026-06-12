"""Generated from Smithy shape ``com.amazonaws.costexplorer#UtilizationByTime``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.reservation_aggregates
    import aws_sdk_cost_explorer.types.reservation_utilization_groups


class UtilizationByTime(TypedDict):
    time_period: NotRequired["aws_sdk_cost_explorer.types.date_interval.DateInterval"]
    """<p>The period of time that this utilization was used for.</p>"""
    groups: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_utilization_groups.ReservationUtilizationGroups"
    ]
    """<p>The groups that this utilization result uses.</p>"""
    total: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_aggregates.ReservationAggregates"
    ]
    """<p>The total number of reservation hours that were used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UtilizationByTime) -> dict:
    out: dict = {}
    if "time_period" in value:
        import aws_sdk_cost_explorer.types.date_interval

        out["TimePeriod"] = (
            aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
                value["time_period"]
            )
        )
    if "groups" in value:
        import aws_sdk_cost_explorer.types.reservation_utilization_groups

        out["Groups"] = (
            aws_sdk_cost_explorer.types.reservation_utilization_groups.serialize_aws_json_1_1(
                value["groups"]
            )
        )
    if "total" in value:
        import aws_sdk_cost_explorer.types.reservation_aggregates

        out["Total"] = (
            aws_sdk_cost_explorer.types.reservation_aggregates.serialize_aws_json_1_1(
                value["total"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UtilizationByTime:
    out: UtilizationByTime = {}  # type: ignore[typeddict-item]
    if "TimePeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["time_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    if "Groups" in data:
        import aws_sdk_cost_explorer.types.reservation_utilization_groups

        out["groups"] = (
            aws_sdk_cost_explorer.types.reservation_utilization_groups.deserialize_aws_json_1_1(
                data["Groups"]
            )
        )
    if "Total" in data:
        import aws_sdk_cost_explorer.types.reservation_aggregates

        out["total"] = (
            aws_sdk_cost_explorer.types.reservation_aggregates.deserialize_aws_json_1_1(
                data["Total"]
            )
        )
    return out
