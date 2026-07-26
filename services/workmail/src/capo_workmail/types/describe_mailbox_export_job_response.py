"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeMailboxExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.description
    import capo_workmail.types.kms_key_arn
    import capo_workmail.types.mailbox_export_error_info
    import capo_workmail.types.mailbox_export_job_state
    import capo_workmail.types.percentage
    import capo_workmail.types.role_arn
    import capo_workmail.types.s3_bucket_name
    import capo_workmail.types.s3_object_key
    import capo_workmail.types.timestamp
    import capo_workmail.types.work_mail_identifier


class DescribeMailboxExportJobResponse(TypedDict, closed=True):
    entity_id: NotRequired[
        "capo_workmail.types.work_mail_identifier.WorkMailIdentifier"
    ]
    """<p>The identifier of the user or resource associated with the mailbox.</p>"""
    description: NotRequired["capo_workmail.types.description.Description"]
    """<p>The mailbox export job description.</p>"""
    role_arn: NotRequired["capo_workmail.types.role_arn.RoleArn"]
    """<p>The ARN of the AWS Identity and Access Management (IAM) role that grants write permission to the Amazon Simple Storage Service (Amazon S3) bucket.</p>"""
    kms_key_arn: NotRequired["capo_workmail.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the symmetric AWS Key Management Service (AWS KMS) key that encrypts the exported mailbox content.</p>"""
    s3_bucket_name: NotRequired["capo_workmail.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the S3 bucket.</p>"""
    s3_prefix: NotRequired["capo_workmail.types.s3_object_key.S3ObjectKey"]
    """<p>The S3 bucket prefix.</p>"""
    s3_path: NotRequired["capo_workmail.types.s3_object_key.S3ObjectKey"]
    """<p>The path to the S3 bucket and file that the mailbox export job is exporting to.</p>"""
    estimated_progress: "capo_workmail.types.percentage.Percentage"
    """<p>The estimated progress of the mailbox export job, in percentage points.</p>"""
    state: NotRequired[
        "capo_workmail.types.mailbox_export_job_state.MailboxExportJobState"
    ]
    """<p>The state of the mailbox export job.</p>"""
    error_info: NotRequired[
        "capo_workmail.types.mailbox_export_error_info.MailboxExportErrorInfo"
    ]
    """<p>Error information for failed mailbox export jobs.</p>"""
    start_time: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The mailbox export job start timestamp.</p>"""
    end_time: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The mailbox export job end timestamp.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMailboxExportJobResponse) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_prefix" in value:
        out["S3Prefix"] = value["s3_prefix"]
    if "s3_path" in value:
        out["S3Path"] = value["s3_path"]
    out["EstimatedProgress"] = value.get("estimated_progress", 0)
    if "state" in value:
        import capo_workmail.types.mailbox_export_job_state

        out["State"] = (
            capo_workmail.types.mailbox_export_job_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "error_info" in value:
        out["ErrorInfo"] = value["error_info"]
    if "start_time" in value:
        import capo_workmail.types.timestamp

        out["StartTime"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_workmail.types.timestamp

        out["EndTime"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMailboxExportJobResponse:
    out: DescribeMailboxExportJobResponse = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "S3Prefix" in data:
        out["s3_prefix"] = data["S3Prefix"]
    if "S3Path" in data:
        out["s3_path"] = data["S3Path"]
    if "EstimatedProgress" in data:
        out["estimated_progress"] = data["EstimatedProgress"]
    else:
        out["estimated_progress"] = 0
    if "State" in data:
        import capo_workmail.types.mailbox_export_job_state

        out["state"] = (
            capo_workmail.types.mailbox_export_job_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "ErrorInfo" in data:
        out["error_info"] = data["ErrorInfo"]
    if "StartTime" in data:
        import capo_workmail.types.timestamp

        out["start_time"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_workmail.types.timestamp

        out["end_time"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
