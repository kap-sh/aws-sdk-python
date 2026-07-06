"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#VectorEnrichmentJobErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_error_type


class VectorEnrichmentJobErrorDetails(TypedDict, closed=True):
    error_type: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_error_type.VectorEnrichmentJobErrorType"
    ]
    """<p>The type of error generated during the Vector Enrichment job.</p>"""
    error_message: NotRequired["str"]
    """<p>A message that you define and then is processed and rendered by the Vector Enrichment job when the error occurs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorEnrichmentJobErrorDetails) -> dict:
    out: dict = {}
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> VectorEnrichmentJobErrorDetails:
    out: VectorEnrichmentJobErrorDetails = {}  # type: ignore[typeddict-item]
    if "ErrorType" in data:
        out["error_type"] = data["ErrorType"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
