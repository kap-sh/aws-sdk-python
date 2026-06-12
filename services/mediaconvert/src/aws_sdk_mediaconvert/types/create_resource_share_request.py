"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CreateResourceShareRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class CreateResourceShareRequest(TypedDict):
    job_id: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Specify MediaConvert Job ID or ARN to share"""
    support_case_id: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """AWS Support case identifier"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceShareRequest) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "support_case_id" in value:
        out["supportCaseId"] = value["support_case_id"]
    return out


def deserialize_json(data: dict) -> CreateResourceShareRequest:
    out: CreateResourceShareRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "supportCaseId" in data:
        out["support_case_id"] = data["supportCaseId"]
    return out
