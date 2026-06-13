"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetVectorEnrichmentJobInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn


class GetVectorEnrichmentJobInput(TypedDict):
    arn: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn"
    """<p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVectorEnrichmentJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVectorEnrichmentJobInput:
    out: GetVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
    return out
