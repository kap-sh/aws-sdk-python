"""Generated from Smithy shape ``com.amazonaws.omics#GetVariantImportRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.resource_id


class GetVariantImportRequest(TypedDict):
    job_id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVariantImportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVariantImportRequest:
    out: GetVariantImportRequest = {}  # type: ignore[typeddict-item]
    return out
