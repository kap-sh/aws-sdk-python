"""Generated from Smithy shape ``com.amazonaws.finspacedata#PermissionGroupByUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.permission_group_id
    import aws_sdk_finspace_data.types.permission_group_membership_status
    import aws_sdk_finspace_data.types.permission_group_name


class PermissionGroupByUser(TypedDict, closed=True):
    permission_group_id: NotRequired[
        "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId"
    ]
    """<p>The unique identifier for the permission group.</p>"""
    name: NotRequired[
        "aws_sdk_finspace_data.types.permission_group_name.PermissionGroupName"
    ]
    """<p>The name of the permission group.</p>"""
    membership_status: NotRequired[
        "aws_sdk_finspace_data.types.permission_group_membership_status.PermissionGroupMembershipStatus"
    ]
    """<p>Indicates the status of the user within a permission group.</p> <ul> <li> <p> <code>ADDITION_IN_PROGRESS</code> – The user is currently being added to the permission group.</p> </li> <li> <p> <code>ADDITION_SUCCESS</code> – The user is successfully added to the permission group.</p> </li> <li> <p> <code>REMOVAL_IN_PROGRESS</code> – The user is currently being removed from the permission group.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionGroupByUser) -> dict:
    out: dict = {}
    if "permission_group_id" in value:
        out["permissionGroupId"] = value["permission_group_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "membership_status" in value:
        import aws_sdk_finspace_data.types.permission_group_membership_status

        out["membershipStatus"] = (
            aws_sdk_finspace_data.types.permission_group_membership_status.serialize_json(
                value["membership_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionGroupByUser:
    out: PermissionGroupByUser = {}  # type: ignore[typeddict-item]
    if "permissionGroupId" in data:
        out["permission_group_id"] = data["permissionGroupId"]
    if "name" in data:
        out["name"] = data["name"]
    if "membershipStatus" in data:
        import aws_sdk_finspace_data.types.permission_group_membership_status

        out["membership_status"] = (
            aws_sdk_finspace_data.types.permission_group_membership_status.deserialize_json(
                data["membershipStatus"]
            )
        )
    return out
