"""Generated from Smithy shape ``com.amazonaws.connectcases#ListLayoutsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.max_results
    import aws_sdk_connectcases.types.next_token


class ListLayoutsRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    max_results: NotRequired["aws_sdk_connectcases.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLayoutsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLayoutsRequest:
    out: ListLayoutsRequest = {}  # type: ignore[typeddict-item]
    return out
