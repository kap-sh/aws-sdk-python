"""Generated from Smithy shape ``com.amazonaws.backup#UpdateReportPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.report_plan_name
    import aws_sdk_backup.types.timestamp


class UpdateReportPlanOutput(TypedDict, closed=True):
    report_plan_name: NotRequired[
        "aws_sdk_backup.types.report_plan_name.ReportPlanName"
    ]
    """<p>The unique name of the report plan.</p>"""
    report_plan_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""
    creation_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time that a report plan is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReportPlanOutput) -> dict:
    out: dict = {}
    if "report_plan_name" in value:
        out["ReportPlanName"] = value["report_plan_name"]
    if "report_plan_arn" in value:
        out["ReportPlanArn"] = value["report_plan_arn"]
    if "creation_time" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> UpdateReportPlanOutput:
    out: UpdateReportPlanOutput = {}  # type: ignore[typeddict-item]
    if "ReportPlanName" in data:
        out["report_plan_name"] = data["ReportPlanName"]
    if "ReportPlanArn" in data:
        out["report_plan_arn"] = data["ReportPlanArn"]
    if "CreationTime" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    return out
