"""Generated from Smithy shape ``com.amazonaws.backup#ReportJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.report_destination
    import aws_sdk_backup.types.report_job_id
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class ReportJob(TypedDict, closed=True):
    report_job_id: NotRequired["aws_sdk_backup.types.report_job_id.ReportJobId"]
    """<p>The identifier for a report job. A unique, randomly generated, Unicode, UTF-8 encoded string that is at most 1,024 bytes long. Report job IDs cannot be edited.</p>"""
    report_plan_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""
    report_template: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Identifies the report template for the report. Reports are built using a report template. The report templates are: </p> <p> <code>RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT</code> </p>"""
    creation_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time that a report job is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    completion_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time that a report job is completed, in Unix format and Coordinated Universal Time (UTC). The value of <code>CompletionTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    status: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The status of a report job. The statuses are:</p> <p> <code>CREATED | RUNNING | COMPLETED | FAILED</code> </p> <p> <code>COMPLETED</code> means that the report is available for your review at your designated destination. If the status is <code>FAILED</code>, review the <code>StatusMessage</code> for the reason.</p>"""
    status_message: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A message explaining the status of the report job.</p>"""
    report_destination: NotRequired[
        "aws_sdk_backup.types.report_destination.ReportDestination"
    ]
    """<p>The S3 bucket name and S3 keys for the destination where the report job publishes the report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportJob) -> dict:
    out: dict = {}
    if "report_job_id" in value:
        out["ReportJobId"] = value["report_job_id"]
    if "report_plan_arn" in value:
        out["ReportPlanArn"] = value["report_plan_arn"]
    if "report_template" in value:
        out["ReportTemplate"] = value["report_template"]
    if "creation_time" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "completion_time" in value:
        import aws_sdk_backup.types.timestamp

        out["CompletionTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["completion_time"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "report_destination" in value:
        import aws_sdk_backup.types.report_destination

        out["ReportDestination"] = (
            aws_sdk_backup.types.report_destination.serialize_json(
                value["report_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReportJob:
    out: ReportJob = {}  # type: ignore[typeddict-item]
    if "ReportJobId" in data:
        out["report_job_id"] = data["ReportJobId"]
    if "ReportPlanArn" in data:
        out["report_plan_arn"] = data["ReportPlanArn"]
    if "ReportTemplate" in data:
        out["report_template"] = data["ReportTemplate"]
    if "CreationTime" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "CompletionTime" in data:
        import aws_sdk_backup.types.timestamp

        out["completion_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CompletionTime"]
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "ReportDestination" in data:
        import aws_sdk_backup.types.report_destination

        out["report_destination"] = (
            aws_sdk_backup.types.report_destination.deserialize_json(
                data["ReportDestination"]
            )
        )
    return out
