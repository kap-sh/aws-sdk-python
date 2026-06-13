"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListDomainsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.max_list_domains_results
    import aws_sdk_controlcatalog.types.pagination_token


class ListDomainsRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_controlcatalog.types.max_list_domains_results.MaxListDomainsResults"
    ]
    """<p>The maximum number of results on a page or for an API request call.</p>"""
    next_token: NotRequired[
        "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainsRequest:
    out: ListDomainsRequest = {}  # type: ignore[typeddict-item]
    return out
