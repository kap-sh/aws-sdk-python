"""Generated from Smithy shape ``com.amazonaws.mgn#StartImportFileEnrichmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.import_file_enrichment_job_id


class StartImportFileEnrichmentResponse(TypedDict, closed=True):
    job_id: NotRequired[
        "aws_sdk_mgn.types.import_file_enrichment_job_id.ImportFileEnrichmentJobID"
    ]
    """<p>The unique identifier of the import file enrichment job that was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportFileEnrichmentResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> StartImportFileEnrichmentResponse:
    out: StartImportFileEnrichmentResponse = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    return out
