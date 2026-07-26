"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StartVectorEnrichmentJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.tags
    import capo_sagemaker_geospatial.types.vector_enrichment_job_arn
    import capo_sagemaker_geospatial.types.vector_enrichment_job_config
    import capo_sagemaker_geospatial.types.vector_enrichment_job_input_config
    import capo_sagemaker_geospatial.types.vector_enrichment_job_status
    import capo_sagemaker_geospatial.types.vector_enrichment_job_type


class StartVectorEnrichmentJobOutput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the Vector Enrichment job.</p>"""
    arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn"
    """<p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>"""
    type: "capo_sagemaker_geospatial.types.vector_enrichment_job_type.VectorEnrichmentJobType"
    """<p>The type of the Vector Enrichment job.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time.</p>"""
    duration_in_seconds: "int"
    """<p>The duration of the Vector Enrichment job, in seconds.</p>"""
    status: "capo_sagemaker_geospatial.types.vector_enrichment_job_status.VectorEnrichmentJobStatus"
    """<p>The status of the Vector Enrichment job being started.</p>"""
    kms_key_id: NotRequired["capo_sagemaker_geospatial.types.kms_key.KmsKey"]
    """<p>The Key Management Service key ID for server-side encryption.</p>"""
    input_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_input_config.VectorEnrichmentJobInputConfig"
    """<p>Input configuration information for starting the Vector Enrichment job.</p>"""
    job_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_config.VectorEnrichmentJobConfig"
    """<p>An object containing information about the job configuration.</p>"""
    execution_role_arn: (
        "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>"""
    tags: NotRequired["capo_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartVectorEnrichmentJobOutput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    out["Type"] = value["type"]
    import capo_sagemaker_geospatial.types._prelude.timestamp

    out["CreationTime"] = (
        capo_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    )
    out["DurationInSeconds"] = value["duration_in_seconds"]
    out["Status"] = value["status"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    import capo_sagemaker_geospatial.types.vector_enrichment_job_input_config

    out["InputConfig"] = (
        capo_sagemaker_geospatial.types.vector_enrichment_job_input_config.serialize_json(
            value["input_config"]
        )
    )
    import capo_sagemaker_geospatial.types.vector_enrichment_job_config

    out["JobConfig"] = (
        capo_sagemaker_geospatial.types.vector_enrichment_job_config.serialize_json(
            value["job_config"]
        )
    )
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "tags" in value:
        import capo_sagemaker_geospatial.types.tags

        out["Tags"] = capo_sagemaker_geospatial.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartVectorEnrichmentJobOutput:
    out: StartVectorEnrichmentJobOutput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartVectorEnrichmentJobOutput.name required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("StartVectorEnrichmentJobOutput.arn required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("StartVectorEnrichmentJobOutput.type required")
    if "CreationTime" in data:
        import capo_sagemaker_geospatial.types._prelude.timestamp

        out["creation_time"] = (
            capo_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    else:
        raise DeserializationError(
            "StartVectorEnrichmentJobOutput.creation_time required"
        )
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    else:
        raise DeserializationError(
            "StartVectorEnrichmentJobOutput.duration_in_seconds required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("StartVectorEnrichmentJobOutput.status required")
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "InputConfig" in data:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_input_config

        out["input_config"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_input_config.deserialize_json(
                data["InputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartVectorEnrichmentJobOutput.input_config required"
        )
    if "JobConfig" in data:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_config

        out["job_config"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_config.deserialize_json(
                data["JobConfig"]
            )
        )
    else:
        raise DeserializationError("StartVectorEnrichmentJobOutput.job_config required")
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError(
            "StartVectorEnrichmentJobOutput.execution_role_arn required"
        )
    if "Tags" in data:
        import capo_sagemaker_geospatial.types.tags

        out["tags"] = capo_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
