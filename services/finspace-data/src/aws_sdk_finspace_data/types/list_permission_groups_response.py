"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListPermissionGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.pagination_token
    import aws_sdk_finspace_data.types.permission_group_list


class ListPermissionGroupsResponse(TypedDict):
    permission_groups: NotRequired[
        "aws_sdk_finspace_data.types.permission_group_list.PermissionGroupList"
    ]
    """<p>A list of all the permission groups.</p>"""
    next_token: NotRequired[
        "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
    ]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionGroupsResponse) -> dict:
    out: dict = {}
    if "permission_groups" in value:
        import aws_sdk_finspace_data.types.permission_group_list

        out["permissionGroups"] = (
            aws_sdk_finspace_data.types.permission_group_list.serialize_json(
                value["permission_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPermissionGroupsResponse:
    out: ListPermissionGroupsResponse = {}  # type: ignore[typeddict-item]
    if "permissionGroups" in data:
        import aws_sdk_finspace_data.types.permission_group_list

        out["permission_groups"] = (
            aws_sdk_finspace_data.types.permission_group_list.deserialize_json(
                data["permissionGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
