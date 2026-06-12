"""Generated from Smithy shape ``com.amazonaws.translate#StopTextTranslationJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_translate.types.job_id
    import aws_sdk_translate.types.job_status


class StopTextTranslationJobResponse(TypedDict):
    job_id: NotRequired["aws_sdk_translate.types.job_id.JobId"]
    """<p>The job ID of the stopped batch translation job.</p>"""
    job_status: NotRequired["aws_sdk_translate.types.job_status.JobStatus"]
    """<p>The status of the designated job. Upon successful completion, the job's status will be <code>STOPPED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTextTranslationJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_status" in value:
        import aws_sdk_translate.types.job_status

        out["JobStatus"] = aws_sdk_translate.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTextTranslationJobResponse:
    out: StopTextTranslationJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobStatus" in data:
        import aws_sdk_translate.types.job_status

        out["job_status"] = aws_sdk_translate.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    return out
