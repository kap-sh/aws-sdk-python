"""Generated from Smithy shape ``com.amazonaws.sesv2#GetImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.job_id


class GetImportJobRequest(TypedDict, closed=True):
    job_id: "capo_sesv2.types.job_id.JobId"
    """<p>The ID of the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImportJobRequest:
    out: GetImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
