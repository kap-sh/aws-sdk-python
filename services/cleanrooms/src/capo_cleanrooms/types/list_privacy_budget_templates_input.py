"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListPrivacyBudgetTemplatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token


class ListPrivacyBudgetTemplatesInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for one of your memberships for a collaboration. The privacy budget templates are retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["capo_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivacyBudgetTemplatesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPrivacyBudgetTemplatesInput:
    out: ListPrivacyBudgetTemplatesInput = {}  # type: ignore[typeddict-item]
    return out
