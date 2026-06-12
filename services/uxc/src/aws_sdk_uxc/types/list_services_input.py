"""Generated from Smithy shape ``com.amazonaws.uxc#ListServicesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_uxc.types.max_results
    import aws_sdk_uxc.types.next_token


class ListServicesInput(TypedDict):
    next_token: NotRequired["aws_sdk_uxc.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results. Use the <code>nextToken</code> value from a previous response.</p>"""
    max_results: NotRequired["aws_sdk_uxc.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServicesInput:
    out: ListServicesInput = {}  # type: ignore[typeddict-item]
    return out
