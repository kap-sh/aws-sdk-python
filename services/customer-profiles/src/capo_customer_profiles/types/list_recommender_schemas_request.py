"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRecommenderSchemasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.token


class ListRecommenderSchemasRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of recommender schemas to return in the response. The default value is 100.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>A token received from a previous ListRecommenderSchemas call to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommenderSchemasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecommenderSchemasRequest:
    out: ListRecommenderSchemasRequest = {}  # type: ignore[typeddict-item]
    return out
