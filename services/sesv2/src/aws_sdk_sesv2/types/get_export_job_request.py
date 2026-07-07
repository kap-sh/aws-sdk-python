"""Generated from Smithy shape ``com.amazonaws.sesv2#GetExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.job_id


class GetExportJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_sesv2.types.job_id.JobId"
    """<p>The export job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExportJobRequest:
    out: GetExportJobRequest = {}  # type: ignore[typeddict-item]
    return out
