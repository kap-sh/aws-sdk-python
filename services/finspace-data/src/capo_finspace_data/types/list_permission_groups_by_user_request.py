"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListPermissionGroupsByUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.pagination_token
    import capo_finspace_data.types.result_limit
    import capo_finspace_data.types.user_id


class ListPermissionGroupsByUserRequest(TypedDict, closed=True):
    user_id: "capo_finspace_data.types.user_id.UserId"
    """<p>The unique identifier for the user.</p>"""
    next_token: NotRequired["capo_finspace_data.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""
    max_results: "capo_finspace_data.types.result_limit.ResultLimit"
    """<p>The maximum number of results per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionGroupsByUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPermissionGroupsByUserRequest:
    out: ListPermissionGroupsByUserRequest = {}  # type: ignore[typeddict-item]
    return out
