"""Generated from Smithy shape ``com.amazonaws.omics#CancelVariantImportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.resource_id


class CancelVariantImportRequest(TypedDict, closed=True):
    job_id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelVariantImportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelVariantImportRequest:
    out: CancelVariantImportRequest = {}  # type: ignore[typeddict-item]
    return out
