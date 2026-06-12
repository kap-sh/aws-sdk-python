"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchPrediction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.async_job_status
    import aws_sdk_frauddetector.types.float_version_string
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.iam_role_arn
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.integer
    import aws_sdk_frauddetector.types.s3_bucket_location
    import aws_sdk_frauddetector.types.string
    import aws_sdk_frauddetector.types.time


class BatchPrediction(TypedDict):
    job_id: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The job ID for the batch prediction.</p>"""
    status: NotRequired["aws_sdk_frauddetector.types.async_job_status.AsyncJobStatus"]
    """<p>The batch prediction status.</p>"""
    failure_reason: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The reason a batch prediction job failed.</p>"""
    start_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of when the batch prediction job started.</p>"""
    completion_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of when the batch prediction job completed.</p>"""
    last_heartbeat_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of most recent heartbeat indicating the batch prediction job was making progress.</p>"""
    input_path: NotRequired[
        "aws_sdk_frauddetector.types.s3_bucket_location.s3BucketLocation"
    ]
    """<p>The Amazon S3 location of your training file.</p>"""
    output_path: NotRequired[
        "aws_sdk_frauddetector.types.s3_bucket_location.s3BucketLocation"
    ]
    """<p>The Amazon S3 location of your output file.</p>"""
    event_type_name: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The name of the event type.</p>"""
    detector_name: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The name of the detector.</p>"""
    detector_version: NotRequired[
        "aws_sdk_frauddetector.types.float_version_string.floatVersionString"
    ]
    """<p>The detector version. </p>"""
    iam_role_arn: NotRequired["aws_sdk_frauddetector.types.iam_role_arn.iamRoleArn"]
    """<p>The ARN of the IAM role to use for this job request.</p>"""
    arn: NotRequired["aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The ARN of batch prediction job.</p>"""
    processed_records_count: NotRequired["aws_sdk_frauddetector.types.integer.Integer"]
    """<p>The number of records processed by the batch prediction job.</p>"""
    total_records_count: NotRequired["aws_sdk_frauddetector.types.integer.Integer"]
    """<p>The total number of records in the batch prediction job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchPrediction) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "status" in value:
        import aws_sdk_frauddetector.types.async_job_status

        out["status"] = (
            aws_sdk_frauddetector.types.async_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "completion_time" in value:
        out["completionTime"] = value["completion_time"]
    if "last_heartbeat_time" in value:
        out["lastHeartbeatTime"] = value["last_heartbeat_time"]
    if "input_path" in value:
        out["inputPath"] = value["input_path"]
    if "output_path" in value:
        out["outputPath"] = value["output_path"]
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "detector_name" in value:
        out["detectorName"] = value["detector_name"]
    if "detector_version" in value:
        out["detectorVersion"] = value["detector_version"]
    if "iam_role_arn" in value:
        out["iamRoleArn"] = value["iam_role_arn"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "processed_records_count" in value:
        out["processedRecordsCount"] = value["processed_records_count"]
    if "total_records_count" in value:
        out["totalRecordsCount"] = value["total_records_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchPrediction:
    out: BatchPrediction = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "status" in data:
        import aws_sdk_frauddetector.types.async_job_status

        out["status"] = (
            aws_sdk_frauddetector.types.async_job_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    if "completionTime" in data:
        out["completion_time"] = data["completionTime"]
    if "lastHeartbeatTime" in data:
        out["last_heartbeat_time"] = data["lastHeartbeatTime"]
    if "inputPath" in data:
        out["input_path"] = data["inputPath"]
    if "outputPath" in data:
        out["output_path"] = data["outputPath"]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    if "detectorName" in data:
        out["detector_name"] = data["detectorName"]
    if "detectorVersion" in data:
        out["detector_version"] = data["detectorVersion"]
    if "iamRoleArn" in data:
        out["iam_role_arn"] = data["iamRoleArn"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "processedRecordsCount" in data:
        out["processed_records_count"] = data["processedRecordsCount"]
    if "totalRecordsCount" in data:
        out["total_records_count"] = data["totalRecordsCount"]
    return out
