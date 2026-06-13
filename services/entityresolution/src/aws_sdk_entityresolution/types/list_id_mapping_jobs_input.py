"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListIdMappingJobsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name_or_id_mapping_workflow_arn
    import aws_sdk_entityresolution.types.next_token


class ListIdMappingJobsInput(TypedDict):
    workflow_name: "aws_sdk_entityresolution.types.entity_name_or_id_mapping_workflow_arn.EntityNameOrIdMappingWorkflowArn"
    """<p>The name of the workflow to be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of objects returned per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdMappingJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdMappingJobsInput:
    out: ListIdMappingJobsInput = {}  # type: ignore[typeddict-item]
    return out
