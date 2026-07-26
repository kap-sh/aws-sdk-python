"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListSavingsPlansPurchaseRecommendationGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generation_summary_list
    import capo_cost_explorer.types.next_page_token


class ListSavingsPlansPurchaseRecommendationGenerationResponse(TypedDict, closed=True):
    generation_summary_list: NotRequired[
        "capo_cost_explorer.types.generation_summary_list.GenerationSummaryList"
    ]
    """<p>The list of historical recommendation generations.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListSavingsPlansPurchaseRecommendationGenerationResponse,
) -> dict:
    out: dict = {}
    if "generation_summary_list" in value:
        import capo_cost_explorer.types.generation_summary_list

        out["GenerationSummaryList"] = (
            capo_cost_explorer.types.generation_summary_list.serialize_aws_json_1_1(
                value["generation_summary_list"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListSavingsPlansPurchaseRecommendationGenerationResponse:
    out: ListSavingsPlansPurchaseRecommendationGenerationResponse = {}  # type: ignore[typeddict-item]
    if "GenerationSummaryList" in data:
        import capo_cost_explorer.types.generation_summary_list

        out["generation_summary_list"] = (
            capo_cost_explorer.types.generation_summary_list.deserialize_aws_json_1_1(
                data["GenerationSummaryList"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
