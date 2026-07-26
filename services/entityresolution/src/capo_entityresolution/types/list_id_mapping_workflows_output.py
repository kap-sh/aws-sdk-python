"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListIdMappingWorkflowsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.id_mapping_workflow_list
    import capo_entityresolution.types.next_token


class ListIdMappingWorkflowsOutput(TypedDict, closed=True):
    workflow_summaries: NotRequired[
        "capo_entityresolution.types.id_mapping_workflow_list.IdMappingWorkflowList"
    ]
    """<p>A list of <code>IdMappingWorkflowSummary</code> objects.</p>"""
    next_token: NotRequired["capo_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdMappingWorkflowsOutput) -> dict:
    out: dict = {}
    if "workflow_summaries" in value:
        import capo_entityresolution.types.id_mapping_workflow_list

        out["workflowSummaries"] = (
            capo_entityresolution.types.id_mapping_workflow_list.serialize_json(
                value["workflow_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIdMappingWorkflowsOutput:
    out: ListIdMappingWorkflowsOutput = {}  # type: ignore[typeddict-item]
    if "workflowSummaries" in data:
        import capo_entityresolution.types.id_mapping_workflow_list

        out["workflow_summaries"] = (
            capo_entityresolution.types.id_mapping_workflow_list.deserialize_json(
                data["workflowSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
