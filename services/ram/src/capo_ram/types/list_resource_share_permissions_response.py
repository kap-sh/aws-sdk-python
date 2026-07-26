"""Generated from Smithy shape ``com.amazonaws.ram#ListResourceSharePermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.resource_share_permission_list
    import capo_ram.types.string


class ListResourceSharePermissionsResponse(TypedDict, closed=True):
    permissions: NotRequired[
        "capo_ram.types.resource_share_permission_list.ResourceSharePermissionList"
    ]
    """<p>An array of objects that describe the permissions associated with the resource share.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceSharePermissionsResponse) -> dict:
    out: dict = {}
    if "permissions" in value:
        import capo_ram.types.resource_share_permission_list

        out["permissions"] = (
            capo_ram.types.resource_share_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceSharePermissionsResponse:
    out: ListResourceSharePermissionsResponse = {}  # type: ignore[typeddict-item]
    if "permissions" in data:
        import capo_ram.types.resource_share_permission_list

        out["permissions"] = (
            capo_ram.types.resource_share_permission_list.deserialize_json(
                data["permissions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
