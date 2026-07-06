"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#VectorEnrichmentJobExportErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_export_error_type


class VectorEnrichmentJobExportErrorDetails(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_export_error_type.VectorEnrichmentJobExportErrorType"
    ]
    """<p>The output error details for an Export operation on a Vector Enrichment job.</p>"""
    message: NotRequired["str"]
    """<p>The message providing details about the errors generated during the Vector Enrichment job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorEnrichmentJobExportErrorDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> VectorEnrichmentJobExportErrorDetails:
    out: VectorEnrichmentJobExportErrorDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
