"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRecommendersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.list_recommenders_request_max_results_integer
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.token


class ListRecommendersRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    max_results: NotRequired[
        "aws_sdk_customer_profiles.types.list_recommenders_request_max_results_integer.ListRecommendersRequestMaxResultsInteger"
    ]
    """<p>The maximum number of recommenders to return in the response. The default value is 100.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>A token received from a previous ListRecommenders call to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecommendersRequest:
    out: ListRecommendersRequest = {}  # type: ignore[typeddict-item]
    return out
