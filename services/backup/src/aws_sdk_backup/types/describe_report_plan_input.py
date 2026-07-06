"""Generated from Smithy shape ``com.amazonaws.backup#DescribeReportPlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.report_plan_name


class DescribeReportPlanInput(TypedDict, closed=True):
    report_plan_name: "aws_sdk_backup.types.report_plan_name.ReportPlanName"
    """<p>The unique name of a report plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReportPlanInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeReportPlanInput:
    out: DescribeReportPlanInput = {}  # type: ignore[typeddict-item]
    return out
