"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEdgeDeploymentPlansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_deployment_plan_summaries
    import capo_sagemaker.types.next_token


class ListEdgeDeploymentPlansResponse(TypedDict, closed=True):
    edge_deployment_plan_summaries: NotRequired[
        "capo_sagemaker.types.edge_deployment_plan_summaries.EdgeDeploymentPlanSummaries"
    ]
    """<p>List of summaries of edge deployment plans.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The token to use when calling the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEdgeDeploymentPlansResponse) -> dict:
    out: dict = {}
    if "edge_deployment_plan_summaries" in value:
        import capo_sagemaker.types.edge_deployment_plan_summaries

        out["EdgeDeploymentPlanSummaries"] = (
            capo_sagemaker.types.edge_deployment_plan_summaries.serialize_aws_json_1_1(
                value["edge_deployment_plan_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEdgeDeploymentPlansResponse:
    out: ListEdgeDeploymentPlansResponse = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanSummaries" in data:
        import capo_sagemaker.types.edge_deployment_plan_summaries

        out["edge_deployment_plan_summaries"] = (
            capo_sagemaker.types.edge_deployment_plan_summaries.deserialize_aws_json_1_1(
                data["EdgeDeploymentPlanSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
