"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#DeleteVectorEnrichmentJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.vector_enrichment_job_arn


class DeleteVectorEnrichmentJobInput(TypedDict, closed=True):
    arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn"
    """<p>The Amazon Resource Name (ARN) of the Vector Enrichment job being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVectorEnrichmentJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVectorEnrichmentJobInput:
    out: DeleteVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
    return out
