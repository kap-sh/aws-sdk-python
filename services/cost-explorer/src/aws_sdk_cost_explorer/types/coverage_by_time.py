"""Generated from Smithy shape ``com.amazonaws.costexplorer#CoverageByTime``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.coverage
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.reservation_coverage_groups


class CoverageByTime(TypedDict, closed=True):
    time_period: NotRequired["aws_sdk_cost_explorer.types.date_interval.DateInterval"]
    """<p>The period that this coverage was used over.</p>"""
    groups: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_coverage_groups.ReservationCoverageGroups"
    ]
    """<p>The groups of instances that the reservation covered.</p>"""
    total: NotRequired["aws_sdk_cost_explorer.types.coverage.Coverage"]
    """<p>The total reservation coverage, in hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CoverageByTime) -> dict:
    out: dict = {}
    if "time_period" in value:
        import aws_sdk_cost_explorer.types.date_interval

        out["TimePeriod"] = (
            aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
                value["time_period"]
            )
        )
    if "groups" in value:
        import aws_sdk_cost_explorer.types.reservation_coverage_groups

        out["Groups"] = (
            aws_sdk_cost_explorer.types.reservation_coverage_groups.serialize_aws_json_1_1(
                value["groups"]
            )
        )
    if "total" in value:
        import aws_sdk_cost_explorer.types.coverage

        out["Total"] = aws_sdk_cost_explorer.types.coverage.serialize_aws_json_1_1(
            value["total"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CoverageByTime:
    out: CoverageByTime = {}  # type: ignore[typeddict-item]
    if "TimePeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["time_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    if "Groups" in data:
        import aws_sdk_cost_explorer.types.reservation_coverage_groups

        out["groups"] = (
            aws_sdk_cost_explorer.types.reservation_coverage_groups.deserialize_aws_json_1_1(
                data["Groups"]
            )
        )
    if "Total" in data:
        import aws_sdk_cost_explorer.types.coverage

        out["total"] = aws_sdk_cost_explorer.types.coverage.deserialize_aws_json_1_1(
            data["Total"]
        )
    return out
