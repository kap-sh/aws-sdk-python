"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkPackagesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_tnb.types.pagination_token


class ListSolNetworkPackagesInput(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to include in the response.</p>"""
    next_token: NotRequired["aws_sdk_tnb.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkPackagesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSolNetworkPackagesInput:
    out: ListSolNetworkPackagesInput = {}  # type: ignore[typeddict-item]
    return out
