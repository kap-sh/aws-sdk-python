"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRecommenderFiltersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.recommender_filter_summary_list
    import aws_sdk_customer_profiles.types.token


class ListRecommenderFiltersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>A token to retrieve the next page of results. Null if there are no more results to retrieve.</p>"""
    recommender_filters: NotRequired[
        "aws_sdk_customer_profiles.types.recommender_filter_summary_list.RecommenderFilterSummaryList"
    ]
    """<p>A list of recommender filters and their properties in the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommenderFiltersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recommender_filters" in value:
        import aws_sdk_customer_profiles.types.recommender_filter_summary_list

        out["RecommenderFilters"] = (
            aws_sdk_customer_profiles.types.recommender_filter_summary_list.serialize_json(
                value["recommender_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecommenderFiltersResponse:
    out: ListRecommenderFiltersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RecommenderFilters" in data:
        import aws_sdk_customer_profiles.types.recommender_filter_summary_list

        out["recommender_filters"] = (
            aws_sdk_customer_profiles.types.recommender_filter_summary_list.deserialize_json(
                data["RecommenderFilters"]
            )
        )
    return out
