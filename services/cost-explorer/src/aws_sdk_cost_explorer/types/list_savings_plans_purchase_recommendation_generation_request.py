"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListSavingsPlansPurchaseRecommendationGenerationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generation_status
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.recommendation_id_list
    import aws_sdk_cost_explorer.types.recommendations_page_size


class ListSavingsPlansPurchaseRecommendationGenerationRequest(TypedDict):
    generation_status: NotRequired[
        "aws_sdk_cost_explorer.types.generation_status.GenerationStatus"
    ]
    """<p>The status of the recommendation generation.</p>"""
    recommendation_ids: NotRequired[
        "aws_sdk_cost_explorer.types.recommendation_id_list.RecommendationIdList"
    ]
    """<p>The IDs for each specific recommendation.</p>"""
    page_size: (
        "aws_sdk_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
    )
    """<p>The number of recommendations that you want returned in a single response object.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListSavingsPlansPurchaseRecommendationGenerationRequest,
) -> dict:
    out: dict = {}
    if "generation_status" in value:
        import aws_sdk_cost_explorer.types.generation_status

        out["GenerationStatus"] = (
            aws_sdk_cost_explorer.types.generation_status.serialize_aws_json_1_1(
                value["generation_status"]
            )
        )
    if "recommendation_ids" in value:
        import aws_sdk_cost_explorer.types.recommendation_id_list

        out["RecommendationIds"] = (
            aws_sdk_cost_explorer.types.recommendation_id_list.serialize_aws_json_1_1(
                value["recommendation_ids"]
            )
        )
    out["PageSize"] = value.get("page_size", 0)
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListSavingsPlansPurchaseRecommendationGenerationRequest:
    out: ListSavingsPlansPurchaseRecommendationGenerationRequest = {}  # type: ignore[typeddict-item]
    if "GenerationStatus" in data:
        import aws_sdk_cost_explorer.types.generation_status

        out["generation_status"] = (
            aws_sdk_cost_explorer.types.generation_status.deserialize_aws_json_1_1(
                data["GenerationStatus"]
            )
        )
    if "RecommendationIds" in data:
        import aws_sdk_cost_explorer.types.recommendation_id_list

        out["recommendation_ids"] = (
            aws_sdk_cost_explorer.types.recommendation_id_list.deserialize_aws_json_1_1(
                data["RecommendationIds"]
            )
        )
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
