"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetRecommenderFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_filter_name


class GetRecommenderFilterRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_filter_name: (
        "capo_customer_profiles.types.recommender_filter_name.RecommenderFilterName"
    )
    """<p>The name of the recommender filter to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderFilterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommenderFilterRequest:
    out: GetRecommenderFilterRequest = {}  # type: ignore[typeddict-item]
    return out
