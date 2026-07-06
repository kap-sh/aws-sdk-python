"""Generated from Smithy shape ``com.amazonaws.translate#StopTextTranslationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.job_id


class StopTextTranslationJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_translate.types.job_id.JobId"
    """<p>The job ID of the job to be stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTextTranslationJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTextTranslationJobRequest:
    out: StopTextTranslationJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StopTextTranslationJobRequest.job_id required")
    return out
