"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAssetTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.next_token


class ListAssetTypesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Pagination token from a previous response to retrieve the next page of results</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single response</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetTypesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetTypesRequest:
    out: ListAssetTypesRequest = {}  # type: ignore[typeddict-item]
    return out
