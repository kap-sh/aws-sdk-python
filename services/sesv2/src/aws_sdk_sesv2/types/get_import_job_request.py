"""Generated from Smithy shape ``com.amazonaws.sesv2#GetImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.job_id


class GetImportJobRequest(TypedDict):
    job_id: "aws_sdk_sesv2.types.job_id.JobId"
    """<p>The ID of the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImportJobRequest:
    out: GetImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
