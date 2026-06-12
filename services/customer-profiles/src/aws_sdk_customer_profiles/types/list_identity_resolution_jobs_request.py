"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListIdentityResolutionJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.token


class ListIdentityResolutionJobsRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityResolutionJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdentityResolutionJobsRequest:
    out: ListIdentityResolutionJobsRequest = {}  # type: ignore[typeddict-item]
    return out
