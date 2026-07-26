"""Generated from Smithy shape ``com.amazonaws.costexplorer#ResultByTime``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.estimated
    import capo_cost_explorer.types.groups
    import capo_cost_explorer.types.metrics


class ResultByTime(TypedDict, closed=True):
    time_period: NotRequired["capo_cost_explorer.types.date_interval.DateInterval"]
    """<p>The time period that the result covers.</p>"""
    total: NotRequired["capo_cost_explorer.types.metrics.Metrics"]
    """<p>The total amount of cost or usage accrued during the time period.</p>"""
    groups: NotRequired["capo_cost_explorer.types.groups.Groups"]
    """<p>The groups that this time period includes.</p>"""
    estimated: "capo_cost_explorer.types.estimated.Estimated"
    """<p>Determines whether the result is estimated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultByTime) -> dict:
    out: dict = {}
    if "time_period" in value:
        import capo_cost_explorer.types.date_interval

        out["TimePeriod"] = (
            capo_cost_explorer.types.date_interval.serialize_aws_json_1_1(
                value["time_period"]
            )
        )
    if "total" in value:
        import capo_cost_explorer.types.metrics

        out["Total"] = capo_cost_explorer.types.metrics.serialize_aws_json_1_1(
            value["total"]
        )
    if "groups" in value:
        import capo_cost_explorer.types.groups

        out["Groups"] = capo_cost_explorer.types.groups.serialize_aws_json_1_1(
            value["groups"]
        )
    out["Estimated"] = value.get("estimated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultByTime:
    out: ResultByTime = {}  # type: ignore[typeddict-item]
    if "TimePeriod" in data:
        import capo_cost_explorer.types.date_interval

        out["time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    if "Total" in data:
        import capo_cost_explorer.types.metrics

        out["total"] = capo_cost_explorer.types.metrics.deserialize_aws_json_1_1(
            data["Total"]
        )
    if "Groups" in data:
        import capo_cost_explorer.types.groups

        out["groups"] = capo_cost_explorer.types.groups.deserialize_aws_json_1_1(
            data["Groups"]
        )
    if "Estimated" in data:
        out["estimated"] = data["Estimated"]
    else:
        out["estimated"] = False
    return out
