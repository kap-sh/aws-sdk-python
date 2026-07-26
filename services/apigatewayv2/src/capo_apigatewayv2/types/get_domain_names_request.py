"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetDomainNamesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetDomainNamesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The maximum number of elements to be returned for this resource.</p>"""
    next_token: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainNamesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainNamesRequest:
    out: GetDomainNamesRequest = {}  # type: ignore[typeddict-item]
    return out
