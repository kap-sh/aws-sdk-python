"""Generated from Smithy shape ``com.amazonaws.deadline#ListMeteredProductsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.license_endpoint_id
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.next_token


class ListMeteredProductsRequest(TypedDict):
    license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId"
    """<p>The license endpoint ID to include on the list of metered products.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: "aws_sdk_deadline.types.max_results.MaxResults"
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMeteredProductsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMeteredProductsRequest:
    out: ListMeteredProductsRequest = {}  # type: ignore[typeddict-item]
    return out
