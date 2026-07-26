"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportVectorEnrichmentJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config
    import capo_sagemaker_geospatial.types.vector_enrichment_job_arn
    import capo_sagemaker_geospatial.types.vector_enrichment_job_export_status


class ExportVectorEnrichmentJobOutput(TypedDict, closed=True):
    arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn"
    """<p>The Amazon Resource Name (ARN) of the Vector Enrichment job being exported.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time.</p>"""
    execution_role_arn: (
        "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM role with permission to upload to the location in OutputConfig.</p>"""
    export_status: "capo_sagemaker_geospatial.types.vector_enrichment_job_export_status.VectorEnrichmentJobExportStatus"
    """<p>The status of the results the Vector Enrichment job being exported.</p>"""
    output_config: "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.ExportVectorEnrichmentJobOutputConfig"
    """<p>Output location information for exporting Vector Enrichment Job results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportVectorEnrichmentJobOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_sagemaker_geospatial.types._prelude.timestamp

    out["CreationTime"] = (
        capo_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    )
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    out["ExportStatus"] = value["export_status"]
    import capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config

    out["OutputConfig"] = (
        capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.serialize_json(
            value["output_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExportVectorEnrichmentJobOutput:
    out: ExportVectorEnrichmentJobOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ExportVectorEnrichmentJobOutput.arn required")
    if "CreationTime" in data:
        import capo_sagemaker_geospatial.types._prelude.timestamp

        out["creation_time"] = (
            capo_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    else:
        raise DeserializationError(
            "ExportVectorEnrichmentJobOutput.creation_time required"
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError(
            "ExportVectorEnrichmentJobOutput.execution_role_arn required"
        )
    if "ExportStatus" in data:
        out["export_status"] = data["ExportStatus"]
    else:
        raise DeserializationError(
            "ExportVectorEnrichmentJobOutput.export_status required"
        )
    if "OutputConfig" in data:
        import capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config

        out["output_config"] = (
            capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.deserialize_json(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ExportVectorEnrichmentJobOutput.output_config required"
        )
    return out
