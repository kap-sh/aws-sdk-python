"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StopVectorEnrichmentJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.vector_enrichment_job_arn


class StopVectorEnrichmentJobInput(TypedDict, closed=True):
    arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn"
    """<p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopVectorEnrichmentJobInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> StopVectorEnrichmentJobInput:
    out: StopVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("StopVectorEnrichmentJobInput.arn required")
    return out
