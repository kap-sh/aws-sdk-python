"""Generated from Smithy shape ``com.amazonaws.novaact#ListWorkflowDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.next_token
    import aws_sdk_nova_act.types.workflow_definition_summaries


class ListWorkflowDefinitionsResponse(TypedDict, closed=True):
    workflow_definition_summaries: "aws_sdk_nova_act.types.workflow_definition_summaries.WorkflowDefinitionSummaries"
    """<p>A list of summary information for workflow definitions.</p>"""
    next_token: NotRequired["aws_sdk_nova_act.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowDefinitionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.workflow_definition_summaries

    out["workflowDefinitionSummaries"] = (
        aws_sdk_nova_act.types.workflow_definition_summaries.serialize_json(
            value["workflow_definition_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowDefinitionsResponse:
    out: ListWorkflowDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "workflowDefinitionSummaries" in data:
        import aws_sdk_nova_act.types.workflow_definition_summaries

        out["workflow_definition_summaries"] = (
            aws_sdk_nova_act.types.workflow_definition_summaries.deserialize_json(
                data["workflowDefinitionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListWorkflowDefinitionsResponse.workflow_definition_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
