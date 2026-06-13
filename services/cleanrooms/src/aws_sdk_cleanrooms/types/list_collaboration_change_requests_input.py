"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationChangeRequestsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.change_request_status
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.pagination_token


class ListCollaborationChangeRequestsInput(TypedDict):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The identifier of the collaboration that the change request is made against.</p>"""
    status: NotRequired[
        "aws_sdk_cleanrooms.types.change_request_status.ChangeRequestStatus"
    ]
    """<p>A filter to only return change requests with the specified status.</p>"""
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationChangeRequestsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollaborationChangeRequestsInput:
    out: ListCollaborationChangeRequestsInput = {}  # type: ignore[typeddict-item]
    return out
