"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetIdMappingJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name_or_id_mapping_workflow_arn
    import aws_sdk_entityresolution.types.job_id


class GetIdMappingJobInput(TypedDict, closed=True):
    workflow_name: "aws_sdk_entityresolution.types.entity_name_or_id_mapping_workflow_arn.EntityNameOrIdMappingWorkflowArn"
    """<p>The name of the workflow.</p>"""
    job_id: "aws_sdk_entityresolution.types.job_id.JobId"
    """<p>The ID of the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdMappingJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIdMappingJobInput:
    out: GetIdMappingJobInput = {}  # type: ignore[typeddict-item]
    return out
