"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.filterable_member_status
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.pagination_token


class ListCollaborationsInput(TypedDict):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>"""
    member_status: NotRequired[
        "aws_sdk_cleanrooms.types.filterable_member_status.FilterableMemberStatus"
    ]
    """<p>The caller's status in a collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollaborationsInput:
    out: ListCollaborationsInput = {}  # type: ignore[typeddict-item]
    return out
