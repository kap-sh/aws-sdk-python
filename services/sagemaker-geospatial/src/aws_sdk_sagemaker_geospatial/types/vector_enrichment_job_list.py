"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#VectorEnrichmentJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output_config

VectorEnrichmentJobList: TypeAlias = list[
    "aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output_config.ListVectorEnrichmentJobOutputConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: VectorEnrichmentJobList) -> list:
    import aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> VectorEnrichmentJobList:
    import aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output_config

    out: VectorEnrichmentJobList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output_config.deserialize_json(
                item
            )
        )
    return out
