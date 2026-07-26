"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListFlowDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.flow_definition_summaries
    import capo_sagemaker.types.next_token


class ListFlowDefinitionsResponse(TypedDict, closed=True):
    flow_definition_summaries: NotRequired[
        "capo_sagemaker.types.flow_definition_summaries.FlowDefinitionSummaries"
    ]
    """<p>An array of objects describing the flow definitions.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token to resume pagination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFlowDefinitionsResponse) -> dict:
    out: dict = {}
    if "flow_definition_summaries" in value:
        import capo_sagemaker.types.flow_definition_summaries

        out["FlowDefinitionSummaries"] = (
            capo_sagemaker.types.flow_definition_summaries.serialize_aws_json_1_1(
                value["flow_definition_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFlowDefinitionsResponse:
    out: ListFlowDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "FlowDefinitionSummaries" in data:
        import capo_sagemaker.types.flow_definition_summaries

        out["flow_definition_summaries"] = (
            capo_sagemaker.types.flow_definition_summaries.deserialize_aws_json_1_1(
                data["FlowDefinitionSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
