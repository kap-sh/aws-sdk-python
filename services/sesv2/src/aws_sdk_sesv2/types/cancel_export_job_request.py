"""Generated from Smithy shape ``com.amazonaws.sesv2#CancelExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.job_id


class CancelExportJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_sesv2.types.job_id.JobId"
    """<p>The export job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelExportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelExportJobRequest:
    out: CancelExportJobRequest = {}  # type: ignore[typeddict-item]
    return out
