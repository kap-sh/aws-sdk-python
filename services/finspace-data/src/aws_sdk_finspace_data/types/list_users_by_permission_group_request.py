"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListUsersByPermissionGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.pagination_token
    import aws_sdk_finspace_data.types.permission_group_id
    import aws_sdk_finspace_data.types.result_limit


class ListUsersByPermissionGroupRequest(TypedDict):
    permission_group_id: (
        "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId"
    )
    """<p>The unique identifier for the permission group.</p>"""
    next_token: NotRequired[
        "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
    ]
    """<p>A token that indicates where a results page should begin.</p>"""
    max_results: "aws_sdk_finspace_data.types.result_limit.ResultLimit"
    """<p>The maximum number of results per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersByPermissionGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListUsersByPermissionGroupRequest:
    out: ListUsersByPermissionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
