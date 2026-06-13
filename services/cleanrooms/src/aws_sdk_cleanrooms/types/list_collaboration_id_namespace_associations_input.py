"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationIdNamespaceAssociationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.pagination_token


class ListCollaborationIdNamespaceAssociationsInput(TypedDict):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique identifier of the collaboration that contains the ID namespace associations that you want to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.&gt;</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationIdNamespaceAssociationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollaborationIdNamespaceAssociationsInput:
    out: ListCollaborationIdNamespaceAssociationsInput = {}  # type: ignore[typeddict-item]
    return out
