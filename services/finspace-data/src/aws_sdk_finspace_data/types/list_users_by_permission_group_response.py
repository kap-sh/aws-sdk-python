"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListUsersByPermissionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.pagination_token
    import aws_sdk_finspace_data.types.user_by_permission_group_list


class ListUsersByPermissionGroupResponse(TypedDict, closed=True):
    users: NotRequired[
        "aws_sdk_finspace_data.types.user_by_permission_group_list.UserByPermissionGroupList"
    ]
    """<p>Lists details of all users in a specific permission group.</p>"""
    next_token: NotRequired[
        "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
    ]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersByPermissionGroupResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import aws_sdk_finspace_data.types.user_by_permission_group_list

        out["users"] = (
            aws_sdk_finspace_data.types.user_by_permission_group_list.serialize_json(
                value["users"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUsersByPermissionGroupResponse:
    out: ListUsersByPermissionGroupResponse = {}  # type: ignore[typeddict-item]
    if "users" in data:
        import aws_sdk_finspace_data.types.user_by_permission_group_list

        out["users"] = (
            aws_sdk_finspace_data.types.user_by_permission_group_list.deserialize_json(
                data["users"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
