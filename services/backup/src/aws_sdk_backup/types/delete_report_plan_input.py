"""Generated from Smithy shape ``com.amazonaws.backup#DeleteReportPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.report_plan_name


class DeleteReportPlanInput(TypedDict):
    report_plan_name: "aws_sdk_backup.types.report_plan_name.ReportPlanName"
    """<p>The unique name of a report plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReportPlanInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteReportPlanInput:
    out: DeleteReportPlanInput = {}  # type: ignore[typeddict-item]
    return out
