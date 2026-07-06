"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateClassificationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.job_status


class UpdateClassificationJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_macie2.types.__string.__string"
    """<p>The unique identifier for the classification job.</p>"""
    job_status: NotRequired["aws_sdk_macie2.types.job_status.JobStatus"]
    """<p>The new status for the job. Valid values are:</p> <ul><li><p>CANCELLED - Stops the job permanently and cancels it. This value is valid only if the job's current status is IDLE, PAUSED, RUNNING, or USER_PAUSED.</p> <p>If you specify this value and the job's current status is RUNNING, Amazon Macie immediately begins to stop all processing tasks for the job. You can't resume or restart a job after you cancel it.</p></li> <li><p>RUNNING - Resumes the job. This value is valid only if the job's current status is USER_PAUSED.</p> <p>If you paused the job while it was actively running and you specify this value less than 30 days after you paused the job, Macie immediately resumes processing from the point where you paused the job. Otherwise, Macie resumes the job according to the schedule and other settings for the job.</p></li> <li><p>USER_PAUSED - Pauses the job temporarily. This value is valid only if the job's current status is IDLE, PAUSED, or RUNNING. If you specify this value and the job's current status is RUNNING, Macie immediately begins to pause all processing tasks for the job.</p> <p>If you pause a one-time job and you don't resume it within 30 days, the job expires and Macie cancels the job. If you pause a recurring job when its status is RUNNING and you don't resume it within 30 days, the job run expires and Macie cancels the run. To check the expiration date, refer to the UserPausedDetails.jobExpiresAt property.</p></li></ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClassificationJobRequest) -> dict:
    out: dict = {}
    if "job_status" in value:
        import aws_sdk_macie2.types.job_status

        out["jobStatus"] = aws_sdk_macie2.types.job_status.serialize_json(
            value["job_status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateClassificationJobRequest:
    out: UpdateClassificationJobRequest = {}  # type: ignore[typeddict-item]
    if "jobStatus" in data:
        import aws_sdk_macie2.types.job_status

        out["job_status"] = aws_sdk_macie2.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    return out
