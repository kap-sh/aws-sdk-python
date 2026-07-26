"""Generated from Smithy shape ``com.amazonaws.ram#ListPermissionAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.associated_permission_list
    import capo_ram.types.string


class ListPermissionAssociationsResponse(TypedDict, closed=True):
    permissions: NotRequired[
        "capo_ram.types.associated_permission_list.AssociatedPermissionList"
    ]
    """<p>A structure with information about this customer managed permission.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionAssociationsResponse) -> dict:
    out: dict = {}
    if "permissions" in value:
        import capo_ram.types.associated_permission_list

        out["permissions"] = capo_ram.types.associated_permission_list.serialize_json(
            value["permissions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPermissionAssociationsResponse:
    out: ListPermissionAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "permissions" in data:
        import capo_ram.types.associated_permission_list

        out["permissions"] = capo_ram.types.associated_permission_list.deserialize_json(
            data["permissions"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
