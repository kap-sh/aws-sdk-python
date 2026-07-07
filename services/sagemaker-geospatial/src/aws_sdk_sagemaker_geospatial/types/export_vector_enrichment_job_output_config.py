"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportVectorEnrichmentJobOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data


class ExportVectorEnrichmentJobOutputConfig(TypedDict, closed=True):
    s3_data: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data.VectorEnrichmentJobS3Data"
    """<p>The input structure for Amazon S3 data; representing the Amazon S3 location of the input data objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportVectorEnrichmentJobOutputConfig) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data

    out["S3Data"] = (
        aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data.serialize_json(
            value["s3_data"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExportVectorEnrichmentJobOutputConfig:
    out: ExportVectorEnrichmentJobOutputConfig = {}  # type: ignore[typeddict-item]
    if "S3Data" in data:
        import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data

        out["s3_data"] = (
            aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_s3_data.deserialize_json(
                data["S3Data"]
            )
        )
    else:
        raise DeserializationError(
            "ExportVectorEnrichmentJobOutputConfig.s3_data required"
        )
    return out
