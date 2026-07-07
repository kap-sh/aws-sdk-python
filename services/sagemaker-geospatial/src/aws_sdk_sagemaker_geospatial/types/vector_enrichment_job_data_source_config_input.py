"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#VectorEnrichmentJobDataSourceConfigInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data


class _VectorEnrichmentJobDataSourceConfigInput_S3Data(TypedDict, closed=True):
    S3Data: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data.VectorEnrichmentJobS3Data"


VectorEnrichmentJobDataSourceConfigInput: TypeAlias = (
    _VectorEnrichmentJobDataSourceConfigInput_S3Data
)


# --- restJson1 ser/de ---
def serialize_json(value: VectorEnrichmentJobDataSourceConfigInput) -> dict:
    if "S3Data" in value:
        import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data

        return {
            "S3Data": aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data.serialize_json(
                value["S3Data"]
            )
        }
    else:
        raise SerializationError(
            "VectorEnrichmentJobDataSourceConfigInput: no variant present"
        )


def deserialize_json(data: dict) -> VectorEnrichmentJobDataSourceConfigInput:
    if "S3Data" in data:
        import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data

        return {
            "S3Data": aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data.deserialize_json(
                data["S3Data"]
            )
        }
    else:
        raise DeserializationError(
            "VectorEnrichmentJobDataSourceConfigInput: no recognized variant key"
        )
