"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRecommendersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_summary_list
    import capo_customer_profiles.types.token


class ListRecommendersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>A token to retrieve the next page of results. Null if there are no more results to retrieve.</p>"""
    recommenders: NotRequired[
        "capo_customer_profiles.types.recommender_summary_list.RecommenderSummaryList"
    ]
    """<p>A list of recommenders and their properties in the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recommenders" in value:
        import capo_customer_profiles.types.recommender_summary_list

        out["Recommenders"] = (
            capo_customer_profiles.types.recommender_summary_list.serialize_json(
                value["recommenders"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecommendersResponse:
    out: ListRecommendersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Recommenders" in data:
        import capo_customer_profiles.types.recommender_summary_list

        out["recommenders"] = (
            capo_customer_profiles.types.recommender_summary_list.deserialize_json(
                data["Recommenders"]
            )
        )
    return out
