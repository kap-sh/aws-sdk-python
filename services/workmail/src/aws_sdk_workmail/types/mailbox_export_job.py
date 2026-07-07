"""Generated from Smithy shape ``com.amazonaws.workmail#MailboxExportJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.description
    import aws_sdk_workmail.types.mailbox_export_job_id
    import aws_sdk_workmail.types.mailbox_export_job_state
    import aws_sdk_workmail.types.percentage
    import aws_sdk_workmail.types.s3_bucket_name
    import aws_sdk_workmail.types.s3_object_key
    import aws_sdk_workmail.types.timestamp
    import aws_sdk_workmail.types.work_mail_identifier


class MailboxExportJob(TypedDict, closed=True):
    job_id: NotRequired[
        "aws_sdk_workmail.types.mailbox_export_job_id.MailboxExportJobId"
    ]
    """<p>The identifier of the mailbox export job.</p>"""
    entity_id: NotRequired[
        "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier"
    ]
    """<p>The identifier of the user or resource associated with the mailbox.</p>"""
    description: NotRequired["aws_sdk_workmail.types.description.Description"]
    """<p>The mailbox export job description.</p>"""
    s3_bucket_name: NotRequired["aws_sdk_workmail.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the S3 bucket.</p>"""
    s3_path: NotRequired["aws_sdk_workmail.types.s3_object_key.S3ObjectKey"]
    """<p>The path to the S3 bucket and file that the mailbox export job exports to.</p>"""
    estimated_progress: "aws_sdk_workmail.types.percentage.Percentage"
    """<p>The estimated progress of the mailbox export job, in percentage points.</p>"""
    state: NotRequired[
        "aws_sdk_workmail.types.mailbox_export_job_state.MailboxExportJobState"
    ]
    """<p>The state of the mailbox export job.</p>"""
    start_time: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The mailbox export job start timestamp.</p>"""
    end_time: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The mailbox export job end timestamp.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MailboxExportJob) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_path" in value:
        out["S3Path"] = value["s3_path"]
    out["EstimatedProgress"] = value.get("estimated_progress", 0)
    if "state" in value:
        import aws_sdk_workmail.types.mailbox_export_job_state

        out["State"] = (
            aws_sdk_workmail.types.mailbox_export_job_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "start_time" in value:
        import aws_sdk_workmail.types.timestamp

        out["StartTime"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_workmail.types.timestamp

        out["EndTime"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MailboxExportJob:
    out: MailboxExportJob = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "S3Path" in data:
        out["s3_path"] = data["S3Path"]
    if "EstimatedProgress" in data:
        out["estimated_progress"] = data["EstimatedProgress"]
    else:
        out["estimated_progress"] = 0
    if "State" in data:
        import aws_sdk_workmail.types.mailbox_export_job_state

        out["state"] = (
            aws_sdk_workmail.types.mailbox_export_job_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_workmail.types.timestamp

        out["start_time"] = aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_workmail.types.timestamp

        out["end_time"] = aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
