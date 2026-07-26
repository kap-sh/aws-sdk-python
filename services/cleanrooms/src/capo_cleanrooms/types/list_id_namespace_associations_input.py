"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListIdNamespaceAssociationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token


class ListIdNamespaceAssociationsInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID namespace association that you want to view.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["capo_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdNamespaceAssociationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdNamespaceAssociationsInput:
    out: ListIdNamespaceAssociationsInput = {}  # type: ignore[typeddict-item]
    return out
