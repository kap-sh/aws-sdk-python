"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListIdentityResolutionJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.token


class ListIdentityResolutionJobsRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityResolutionJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdentityResolutionJobsRequest:
    out: ListIdentityResolutionJobsRequest = {}  # type: ignore[typeddict-item]
    return out
