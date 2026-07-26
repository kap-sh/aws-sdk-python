"""Generated from Smithy shape ``com.amazonaws.backup#DescribeReportPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.report_plan


class DescribeReportPlanOutput(TypedDict, closed=True):
    report_plan: NotRequired["capo_backup.types.report_plan.ReportPlan"]
    """<p>Returns details about the report plan that is specified by its name. These details include the report plan's Amazon Resource Name (ARN), description, settings, delivery channel, deployment status, creation time, and last attempted and successful run times.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReportPlanOutput) -> dict:
    out: dict = {}
    if "report_plan" in value:
        import capo_backup.types.report_plan

        out["ReportPlan"] = capo_backup.types.report_plan.serialize_json(
            value["report_plan"]
        )
    return out


def deserialize_json(data: dict) -> DescribeReportPlanOutput:
    out: DescribeReportPlanOutput = {}  # type: ignore[typeddict-item]
    if "ReportPlan" in data:
        import capo_backup.types.report_plan

        out["report_plan"] = capo_backup.types.report_plan.deserialize_json(
            data["ReportPlan"]
        )
    return out
