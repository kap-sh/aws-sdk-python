"""Generated from Smithy shape ``com.amazonaws.entityresolution#StartIdMappingJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name_or_id_mapping_workflow_arn
    import capo_entityresolution.types.id_mapping_job_output_source_config
    import capo_entityresolution.types.job_type


class StartIdMappingJobInput(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name_or_id_mapping_workflow_arn.EntityNameOrIdMappingWorkflowArn"
    """<p>The name of the ID mapping job to be retrieved.</p>"""
    output_source_config: NotRequired[
        "capo_entityresolution.types.id_mapping_job_output_source_config.IdMappingJobOutputSourceConfig"
    ]
    """<p>A list of <code>OutputSource</code> objects.</p>"""
    job_type: NotRequired["capo_entityresolution.types.job_type.JobType"]
    """<p> The job type for the ID mapping job.</p> <p>If the <code>jobType</code> value is set to <code>INCREMENTAL</code>, only new or changed data is processed since the last job run. This is the default value if the <code>CreateIdMappingWorkflow</code> API is configured with an <code>incrementalRunConfig</code>.</p> <p>If the <code>jobType</code> value is set to <code>BATCH</code>, all data is processed from the input source, regardless of previous job runs. This is the default value if the <code>CreateIdMappingWorkflow</code> API isn't configured with an <code>incrementalRunConfig</code>.</p> <p>If the <code>jobType</code> value is set to <code>DELETE_ONLY</code>, only deletion requests from <code>BatchDeleteUniqueIds</code> are processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartIdMappingJobInput) -> dict:
    out: dict = {}
    if "output_source_config" in value:
        import capo_entityresolution.types.id_mapping_job_output_source_config

        out["outputSourceConfig"] = (
            capo_entityresolution.types.id_mapping_job_output_source_config.serialize_json(
                value["output_source_config"]
            )
        )
    if "job_type" in value:
        import capo_entityresolution.types.job_type

        out["jobType"] = capo_entityresolution.types.job_type.serialize_json(
            value["job_type"]
        )
    return out


def deserialize_json(data: dict) -> StartIdMappingJobInput:
    out: StartIdMappingJobInput = {}  # type: ignore[typeddict-item]
    if "outputSourceConfig" in data:
        import capo_entityresolution.types.id_mapping_job_output_source_config

        out["output_source_config"] = (
            capo_entityresolution.types.id_mapping_job_output_source_config.deserialize_json(
                data["outputSourceConfig"]
            )
        )
    if "jobType" in data:
        import capo_entityresolution.types.job_type

        out["job_type"] = capo_entityresolution.types.job_type.deserialize_json(
            data["jobType"]
        )
    return out
