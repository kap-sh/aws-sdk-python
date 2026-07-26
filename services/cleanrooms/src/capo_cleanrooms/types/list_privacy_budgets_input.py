"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListPrivacyBudgetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.budgeted_resource_arn
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.privacy_budget_type


class ListPrivacyBudgetsInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for one of your memberships for a collaboration. The privacy budget is retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>"""
    privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    """<p>The privacy budget type.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["capo_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>"""
    access_budget_resource_arn: NotRequired[
        "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the access budget resource to filter privacy budgets by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivacyBudgetsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPrivacyBudgetsInput:
    out: ListPrivacyBudgetsInput = {}  # type: ignore[typeddict-item]
    return out
