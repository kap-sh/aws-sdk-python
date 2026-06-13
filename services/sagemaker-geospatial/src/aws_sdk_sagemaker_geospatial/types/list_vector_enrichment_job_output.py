"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ListVectorEnrichmentJobOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.next_token
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_list


class ListVectorEnrichmentJobOutput(TypedDict):
    vector_enrichment_job_summaries: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_list.VectorEnrichmentJobList"
    """<p>Contains summary information about the Vector Enrichment jobs.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker_geospatial.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorEnrichmentJobOutput) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_list

    out["VectorEnrichmentJobSummaries"] = (
        aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_list.serialize_json(
            value["vector_enrichment_job_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVectorEnrichmentJobOutput:
    out: ListVectorEnrichmentJobOutput = {}  # type: ignore[typeddict-item]
    if "VectorEnrichmentJobSummaries" in data:
        import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_list

        out["vector_enrichment_job_summaries"] = (
            aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_list.deserialize_json(
                data["VectorEnrichmentJobSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListVectorEnrichmentJobOutput.vector_enrichment_job_summaries required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
