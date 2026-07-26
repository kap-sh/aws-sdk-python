"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationPrivacyBudgetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.budgeted_resource_arn
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.privacy_budget_type


class ListCollaborationPrivacyBudgetsInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for one of your collaborations.</p>"""
    privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    """<p>Specifies the type of the privacy budget.</p>"""
    max_results: NotRequired["capo_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    access_budget_resource_arn: NotRequired[
        "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Configured Table Association (ConfiguredTableAssociation) used to filter privacy budgets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationPrivacyBudgetsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollaborationPrivacyBudgetsInput:
    out: ListCollaborationPrivacyBudgetsInput = {}  # type: ignore[typeddict-item]
    return out
