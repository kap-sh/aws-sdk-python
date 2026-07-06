"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationPrivacyBudgetTemplatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.pagination_token


class ListCollaborationPrivacyBudgetTemplatesInput(TypedDict, closed=True):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for one of your collaborations.</p>"""
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationPrivacyBudgetTemplatesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollaborationPrivacyBudgetTemplatesInput:
    out: ListCollaborationPrivacyBudgetTemplatesInput = {}  # type: ignore[typeddict-item]
    return out
