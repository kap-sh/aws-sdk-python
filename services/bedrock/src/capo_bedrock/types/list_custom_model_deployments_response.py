"""Generated from Smithy shape ``com.amazonaws.bedrock#ListCustomModelDeploymentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_deployment_summary_list
    import capo_bedrock.types.pagination_token


class ListCustomModelDeploymentsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of results. This value is null when there are no more results to return.</p>"""
    model_deployment_summaries: NotRequired[
        "capo_bedrock.types.custom_model_deployment_summary_list.CustomModelDeploymentSummaryList"
    ]
    """<p>A list of custom model deployment summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomModelDeploymentsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "model_deployment_summaries" in value:
        import capo_bedrock.types.custom_model_deployment_summary_list

        out["modelDeploymentSummaries"] = (
            capo_bedrock.types.custom_model_deployment_summary_list.serialize_json(
                value["model_deployment_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCustomModelDeploymentsResponse:
    out: ListCustomModelDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("modelDeploymentSummaries") is not None:
        import capo_bedrock.types.custom_model_deployment_summary_list

        out["model_deployment_summaries"] = (
            capo_bedrock.types.custom_model_deployment_summary_list.deserialize_json(
                data["modelDeploymentSummaries"]
            )
        )
    return out
