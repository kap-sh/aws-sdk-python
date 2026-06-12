"""Generated from Smithy shape ``com.amazonaws.voiceid#FraudsterRegistrationJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.failure_details
    import aws_sdk_voice_id.types.fraudster_registration_job_status
    import aws_sdk_voice_id.types.job_id
    import aws_sdk_voice_id.types.job_name
    import aws_sdk_voice_id.types.job_progress
    import aws_sdk_voice_id.types.timestamp


class FraudsterRegistrationJobSummary(TypedDict):
    job_name: NotRequired["aws_sdk_voice_id.types.job_name.JobName"]
    """<p>The client-provided name for the fraudster registration job.</p>"""
    job_id: NotRequired["aws_sdk_voice_id.types.job_id.JobId"]
    """<p>The service-generated identifier for the fraudster registration job.</p>"""
    job_status: NotRequired[
        "aws_sdk_voice_id.types.fraudster_registration_job_status.FraudsterRegistrationJobStatus"
    ]
    """<p>The current status of the fraudster registration job.</p>"""
    domain_id: NotRequired["aws_sdk_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the fraudster registration job.</p>"""
    created_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when the fraudster registration job was created. </p>"""
    ended_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when the fraudster registration job ended.</p>"""
    failure_details: NotRequired[
        "aws_sdk_voice_id.types.failure_details.FailureDetails"
    ]
    """<p>Contains details that are populated when an entire batch job fails. In cases of individual registration job failures, the batch job as a whole doesn't fail; it is completed with a <code>JobStatus</code> of <code>COMPLETED_WITH_ERRORS</code>. You can use the job output file to identify the individual registration requests that failed.</p>"""
    job_progress: NotRequired["aws_sdk_voice_id.types.job_progress.JobProgress"]
    """<p>Shows the completed percentage of registration requests listed in the input file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FraudsterRegistrationJobSummary) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_status" in value:
        out["JobStatus"] = value["job_status"]
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
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


def deserialize_aws_json_1_0(data: dict) -> FraudsterRegistrationJobSummary:
    out: FraudsterRegistrationJobSummary = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobStatus" in data:
        out["job_status"] = data["JobStatus"]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
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
