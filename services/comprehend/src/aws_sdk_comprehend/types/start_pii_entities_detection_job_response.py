"""Generated from Smithy shape ``com.amazonaws.comprehend#StartPiiEntitiesDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_arn
    import aws_sdk_comprehend.types.job_id
    import aws_sdk_comprehend.types.job_status


class StartPiiEntitiesDetectionJobResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_comprehend.types.job_id.JobId"]
    """<p>The identifier generated for the job.</p>"""
    job_arn: NotRequired["aws_sdk_comprehend.types.comprehend_arn.ComprehendArn"]
    """<p>The Amazon Resource Name (ARN) of the PII entity detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:<partition>:comprehend:<region>:<account-id>:pii-entities-detection-job/<job-id></code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>"""
    job_status: NotRequired["aws_sdk_comprehend.types.job_status.JobStatus"]
    """<p>The status of the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartPiiEntitiesDetectionJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    if "job_status" in value:
        import aws_sdk_comprehend.types.job_status

        out["JobStatus"] = aws_sdk_comprehend.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartPiiEntitiesDetectionJobResponse:
    out: StartPiiEntitiesDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobArn" in data:
        out["job_arn"] = data["JobArn"]
    if "JobStatus" in data:
        import aws_sdk_comprehend.types.job_status

        out["job_status"] = (
            aws_sdk_comprehend.types.job_status.deserialize_aws_json_1_1(
                data["JobStatus"]
            )
        )
    return out
