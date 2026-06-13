"""Generated from Smithy shape ``com.amazonaws.backup#ListReportPlansOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.report_plan_list
    import aws_sdk_backup.types.string


class ListReportPlansOutput(TypedDict):
    report_plans: NotRequired["aws_sdk_backup.types.report_plan_list.ReportPlanList"]
    """<p>The report plans with detailed information for each plan. This information includes the Amazon Resource Name (ARN), report plan name, description, settings, delivery channel, deployment status, creation time, and last times the report plan attempted to and successfully ran.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReportPlansOutput) -> dict:
    out: dict = {}
    if "report_plans" in value:
        import aws_sdk_backup.types.report_plan_list

        out["ReportPlans"] = aws_sdk_backup.types.report_plan_list.serialize_json(
            value["report_plans"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReportPlansOutput:
    out: ListReportPlansOutput = {}  # type: ignore[typeddict-item]
    if "ReportPlans" in data:
        import aws_sdk_backup.types.report_plan_list

        out["report_plans"] = aws_sdk_backup.types.report_plan_list.deserialize_json(
            data["ReportPlans"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
