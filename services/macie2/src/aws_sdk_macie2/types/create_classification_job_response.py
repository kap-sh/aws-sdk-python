"""Generated from Smithy shape ``com.amazonaws.macie2#CreateClassificationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class CreateClassificationJobResponse(TypedDict, closed=True):
    job_arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClassificationJobResponse) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> CreateClassificationJobResponse:
    out: CreateClassificationJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    return out
