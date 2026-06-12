"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListPermissionGroupsByUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.pagination_token
    import aws_sdk_finspace_data.types.result_limit
    import aws_sdk_finspace_data.types.user_id


class ListPermissionGroupsByUserRequest(TypedDict):
    user_id: "aws_sdk_finspace_data.types.user_id.UserId"
    """<p>The unique identifier for the user.</p>"""
    next_token: NotRequired[
        "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
    ]
    """<p>A token that indicates where a results page should begin.</p>"""
    max_results: "aws_sdk_finspace_data.types.result_limit.ResultLimit"
    """<p>The maximum number of results per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionGroupsByUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPermissionGroupsByUserRequest:
    out: ListPermissionGroupsByUserRequest = {}  # type: ignore[typeddict-item]
    return out
