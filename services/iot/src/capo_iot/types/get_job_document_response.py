"""Generated from Smithy shape ``com.amazonaws.iot#GetJobDocumentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.job_document


class GetJobDocumentResponse(TypedDict, closed=True):
    document: NotRequired["capo_iot.types.job_document.JobDocument"]
    """<p>The job document content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobDocumentResponse) -> dict:
    out: dict = {}
    if "document" in value:
        out["document"] = value["document"]
    return out


def deserialize_json(data: dict) -> GetJobDocumentResponse:
    out: GetJobDocumentResponse = {}  # type: ignore[typeddict-item]
    if "document" in data:
        out["document"] = data["document"]
    return out
