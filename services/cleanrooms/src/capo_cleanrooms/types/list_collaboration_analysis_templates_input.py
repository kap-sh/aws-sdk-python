"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationAnalysisTemplatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.pagination_token


class ListCollaborationAnalysisTemplatesInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["capo_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationAnalysisTemplatesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollaborationAnalysisTemplatesInput:
    out: ListCollaborationAnalysisTemplatesInput = {}  # type: ignore[typeddict-item]
    return out
