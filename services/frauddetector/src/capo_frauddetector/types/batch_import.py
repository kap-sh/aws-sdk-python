"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchImport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.async_job_status
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.iam_role_arn
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.integer
    import capo_frauddetector.types.s3_bucket_location
    import capo_frauddetector.types.string
    import capo_frauddetector.types.time


class BatchImport(TypedDict, closed=True):
    job_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The ID of the batch import job. </p>"""
    status: NotRequired["capo_frauddetector.types.async_job_status.AsyncJobStatus"]
    """<p>The status of the batch import job.</p>"""
    failure_reason: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The reason batch import job failed.</p>"""
    start_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of when the batch import job started.</p>"""
    completion_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of when batch import job completed.</p>"""
    input_path: NotRequired[
        "capo_frauddetector.types.s3_bucket_location.s3BucketLocation"
    ]
    """<p>The Amazon S3 location of your data file for batch import.</p>"""
    output_path: NotRequired[
        "capo_frauddetector.types.s3_bucket_location.s3BucketLocation"
    ]
    """<p>The Amazon S3 location of your output file.</p>"""
    event_type_name: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The name of the event type.</p>"""
    iam_role_arn: NotRequired["capo_frauddetector.types.iam_role_arn.iamRoleArn"]
    """<p>The ARN of the IAM role to use for this job request.</p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The ARN of the batch import job.</p>"""
    processed_records_count: NotRequired["capo_frauddetector.types.integer.Integer"]
    """<p>The number of records processed by batch import job.</p>"""
    failed_records_count: NotRequired["capo_frauddetector.types.integer.Integer"]
    """<p>The number of records that failed to import. </p>"""
    total_records_count: NotRequired["capo_frauddetector.types.integer.Integer"]
    """<p>The total number of records in the batch import job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchImport) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "status" in value:
        import capo_frauddetector.types.async_job_status

        out["status"] = (
            capo_frauddetector.types.async_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "completion_time" in value:
        out["completionTime"] = value["completion_time"]
    if "input_path" in value:
        out["inputPath"] = value["input_path"]
    if "output_path" in value:
        out["outputPath"] = value["output_path"]
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "iam_role_arn" in value:
        out["iamRoleArn"] = value["iam_role_arn"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "processed_records_count" in value:
        out["processedRecordsCount"] = value["processed_records_count"]
    if "failed_records_count" in value:
        out["failedRecordsCount"] = value["failed_records_count"]
    if "total_records_count" in value:
        out["totalRecordsCount"] = value["total_records_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchImport:
    out: BatchImport = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "status" in data:
        import capo_frauddetector.types.async_job_status

        out["status"] = (
            capo_frauddetector.types.async_job_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    if "completionTime" in data:
        out["completion_time"] = data["completionTime"]
    if "inputPath" in data:
        out["input_path"] = data["inputPath"]
    if "outputPath" in data:
        out["output_path"] = data["outputPath"]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    if "iamRoleArn" in data:
        out["iam_role_arn"] = data["iamRoleArn"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "processedRecordsCount" in data:
        out["processed_records_count"] = data["processedRecordsCount"]
    if "failedRecordsCount" in data:
        out["failed_records_count"] = data["failedRecordsCount"]
    if "totalRecordsCount" in data:
        out["total_records_count"] = data["totalRecordsCount"]
    return out
