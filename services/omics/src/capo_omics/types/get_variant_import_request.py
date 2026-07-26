"""Generated from Smithy shape ``com.amazonaws.omics#GetVariantImportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.resource_id


class GetVariantImportRequest(TypedDict, closed=True):
    job_id: "capo_omics.types.resource_id.ResourceId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVariantImportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVariantImportRequest:
    out: GetVariantImportRequest = {}  # type: ignore[typeddict-item]
    return out
