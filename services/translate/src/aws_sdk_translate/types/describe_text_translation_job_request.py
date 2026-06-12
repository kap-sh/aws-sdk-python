"""Generated from Smithy shape ``com.amazonaws.translate#DescribeTextTranslationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.job_id


class DescribeTextTranslationJobRequest(TypedDict):
    job_id: "aws_sdk_translate.types.job_id.JobId"
    """<p>The identifier that Amazon Translate generated for the job. The <a>StartTextTranslationJob</a> operation returns this identifier in its response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTextTranslationJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTextTranslationJobRequest:
    out: DescribeTextTranslationJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("DescribeTextTranslationJobRequest.job_id required")
    return out
