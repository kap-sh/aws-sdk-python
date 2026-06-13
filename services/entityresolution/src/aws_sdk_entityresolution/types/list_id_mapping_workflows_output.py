"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListIdMappingWorkflowsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_mapping_workflow_list
    import aws_sdk_entityresolution.types.next_token


class ListIdMappingWorkflowsOutput(TypedDict):
    workflow_summaries: NotRequired[
        "aws_sdk_entityresolution.types.id_mapping_workflow_list.IdMappingWorkflowList"
    ]
    """<p>A list of <code>IdMappingWorkflowSummary</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdMappingWorkflowsOutput) -> dict:
    out: dict = {}
    if "workflow_summaries" in value:
        import aws_sdk_entityresolution.types.id_mapping_workflow_list

        out["workflowSummaries"] = (
            aws_sdk_entityresolution.types.id_mapping_workflow_list.serialize_json(
                value["workflow_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIdMappingWorkflowsOutput:
    out: ListIdMappingWorkflowsOutput = {}  # type: ignore[typeddict-item]
    if "workflowSummaries" in data:
        import aws_sdk_entityresolution.types.id_mapping_workflow_list

        out["workflow_summaries"] = (
            aws_sdk_entityresolution.types.id_mapping_workflow_list.deserialize_json(
                data["workflowSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
