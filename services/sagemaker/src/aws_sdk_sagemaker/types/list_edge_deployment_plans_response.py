"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEdgeDeploymentPlansResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_deployment_plan_summaries
    import aws_sdk_sagemaker.types.next_token


class ListEdgeDeploymentPlansResponse(TypedDict):
    edge_deployment_plan_summaries: NotRequired[
        "aws_sdk_sagemaker.types.edge_deployment_plan_summaries.EdgeDeploymentPlanSummaries"
    ]
    """<p>List of summaries of edge deployment plans.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>The token to use when calling the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEdgeDeploymentPlansResponse) -> dict:
    out: dict = {}
    if "edge_deployment_plan_summaries" in value:
        import aws_sdk_sagemaker.types.edge_deployment_plan_summaries

        out["EdgeDeploymentPlanSummaries"] = (
            aws_sdk_sagemaker.types.edge_deployment_plan_summaries.serialize_aws_json_1_1(
                value["edge_deployment_plan_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEdgeDeploymentPlansResponse:
    out: ListEdgeDeploymentPlansResponse = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanSummaries" in data:
        import aws_sdk_sagemaker.types.edge_deployment_plan_summaries

        out["edge_deployment_plan_summaries"] = (
            aws_sdk_sagemaker.types.edge_deployment_plan_summaries.deserialize_aws_json_1_1(
                data["EdgeDeploymentPlanSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
