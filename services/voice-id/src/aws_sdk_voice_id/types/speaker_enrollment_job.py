"""Generated from Smithy shape ``com.amazonaws.voiceid#SpeakerEnrollmentJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.enrollment_config
    import aws_sdk_voice_id.types.failure_details
    import aws_sdk_voice_id.types.iam_role_arn
    import aws_sdk_voice_id.types.input_data_config
    import aws_sdk_voice_id.types.job_id
    import aws_sdk_voice_id.types.job_name
    import aws_sdk_voice_id.types.job_progress
    import aws_sdk_voice_id.types.output_data_config
    import aws_sdk_voice_id.types.speaker_enrollment_job_status
    import aws_sdk_voice_id.types.timestamp


class SpeakerEnrollmentJob(TypedDict):
    job_name: NotRequired["aws_sdk_voice_id.types.job_name.JobName"]
    """<p>The client-provided name for the speaker enrollment job.</p>"""
    job_id: NotRequired["aws_sdk_voice_id.types.job_id.JobId"]
    """<p>The service-generated identifier for the speaker enrollment job.</p>"""
    job_status: NotRequired[
        "aws_sdk_voice_id.types.speaker_enrollment_job_status.SpeakerEnrollmentJobStatus"
    ]
    """<p>The current status of the speaker enrollment job.</p>"""
    domain_id: NotRequired["aws_sdk_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the speaker enrollment job.</p>"""
    data_access_role_arn: NotRequired["aws_sdk_voice_id.types.iam_role_arn.IamRoleArn"]
    """<p>The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the job output file.</p>"""
    enrollment_config: NotRequired[
        "aws_sdk_voice_id.types.enrollment_config.EnrollmentConfig"
    ]
    """<p>The configuration that defines the action to take when the speaker is already enrolled in Voice ID, and the <code>FraudDetectionConfig</code> to use.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_voice_id.types.input_data_config.InputDataConfig"
    ]
    """<p>The input data config containing an S3 URI for the input manifest file that contains the list of speaker enrollment job requests.</p>"""
    output_data_config: NotRequired[
        "aws_sdk_voice_id.types.output_data_config.OutputDataConfig"
    ]
    """<p>The output data config containing the S3 location where Voice ID writes the job output file; you must also include a KMS key ID to encrypt the file.</p>"""
    created_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when the speaker enrollment job was created.</p>"""
    ended_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when the speaker enrollment job ended. </p>"""
    failure_details: NotRequired[
        "aws_sdk_voice_id.types.failure_details.FailureDetails"
    ]
    """<p>Contains details that are populated when an entire batch job fails. In cases of individual registration job failures, the batch job as a whole doesn't fail; it is completed with a <code>JobStatus</code> of <code>COMPLETED_WITH_ERRORS</code>. You can use the job output file to identify the individual registration requests that failed.</p>"""
    job_progress: NotRequired["aws_sdk_voice_id.types.job_progress.JobProgress"]
    """<p>Provides details on job progress. This field shows the completed percentage of registration requests listed in the input file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpeakerEnrollmentJob) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_status" in value:
        out["JobStatus"] = value["job_status"]
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "enrollment_config" in value:
        import aws_sdk_voice_id.types.enrollment_config

        out["EnrollmentConfig"] = (
            aws_sdk_voice_id.types.enrollment_config.serialize_aws_json_1_0(
                value["enrollment_config"]
            )
        )
    if "input_data_config" in value:
        import aws_sdk_voice_id.types.input_data_config

        out["InputDataConfig"] = (
            aws_sdk_voice_id.types.input_data_config.serialize_aws_json_1_0(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import aws_sdk_voice_id.types.output_data_config

        out["OutputDataConfig"] = (
            aws_sdk_voice_id.types.output_data_config.serialize_aws_json_1_0(
                value["output_data_config"]
            )
        )
    if "created_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["CreatedAt"] = aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "ended_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["EndedAt"] = aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["ended_at"]
        )
    if "failure_details" in value:
        import aws_sdk_voice_id.types.failure_details

        out["FailureDetails"] = (
            aws_sdk_voice_id.types.failure_details.serialize_aws_json_1_0(
                value["failure_details"]
            )
        )
    if "job_progress" in value:
        import aws_sdk_voice_id.types.job_progress

        out["JobProgress"] = aws_sdk_voice_id.types.job_progress.serialize_aws_json_1_0(
            value["job_progress"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SpeakerEnrollmentJob:
    out: SpeakerEnrollmentJob = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobStatus" in data:
        out["job_status"] = data["JobStatus"]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "EnrollmentConfig" in data:
        import aws_sdk_voice_id.types.enrollment_config

        out["enrollment_config"] = (
            aws_sdk_voice_id.types.enrollment_config.deserialize_aws_json_1_0(
                data["EnrollmentConfig"]
            )
        )
    if "InputDataConfig" in data:
        import aws_sdk_voice_id.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_voice_id.types.input_data_config.deserialize_aws_json_1_0(
                data["InputDataConfig"]
            )
        )
    if "OutputDataConfig" in data:
        import aws_sdk_voice_id.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_voice_id.types.output_data_config.deserialize_aws_json_1_0(
                data["OutputDataConfig"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["created_at"] = aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if "EndedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["ended_at"] = aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["EndedAt"]
        )
    if "FailureDetails" in data:
        import aws_sdk_voice_id.types.failure_details

        out["failure_details"] = (
            aws_sdk_voice_id.types.failure_details.deserialize_aws_json_1_0(
                data["FailureDetails"]
            )
        )
    if "JobProgress" in data:
        import aws_sdk_voice_id.types.job_progress

        out["job_progress"] = (
            aws_sdk_voice_id.types.job_progress.deserialize_aws_json_1_0(
                data["JobProgress"]
            )
        )
    return out
