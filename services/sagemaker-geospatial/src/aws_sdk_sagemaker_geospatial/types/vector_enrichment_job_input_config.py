"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#VectorEnrichmentJobInputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_document_type


class VectorEnrichmentJobInputConfig(TypedDict):
    document_type: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_document_type.VectorEnrichmentJobDocumentType"
    """<p>The input structure that defines the data source file type.</p>"""
    data_source_config: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input.VectorEnrichmentJobDataSourceConfigInput"
    """<p>The input structure for the data source that represents the storage type of the input data objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorEnrichmentJobInputConfig) -> dict:
    out: dict = {}
    out["DocumentType"] = value["document_type"]
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input

    out["DataSourceConfig"] = (
        aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input.serialize_json(
            value["data_source_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> VectorEnrichmentJobInputConfig:
    out: VectorEnrichmentJobInputConfig = {}  # type: ignore[typeddict-item]
    if "DocumentType" in data:
        out["document_type"] = data["DocumentType"]
    else:
        raise DeserializationError(
            "VectorEnrichmentJobInputConfig.document_type required"
        )
    if "DataSourceConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input

        out["data_source_config"] = (
            aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input.deserialize_json(
                data["DataSourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "VectorEnrichmentJobInputConfig.data_source_config required"
        )
    return out
