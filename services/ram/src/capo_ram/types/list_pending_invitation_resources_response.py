"""Generated from Smithy shape ``com.amazonaws.ram#ListPendingInvitationResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.resource_list
    import capo_ram.types.string


class ListPendingInvitationResourcesResponse(TypedDict, closed=True):
    resources: NotRequired["capo_ram.types.resource_list.ResourceList"]
    """<p>An array of objects that contain the information about the resources included the specified resource share.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPendingInvitationResourcesResponse) -> dict:
    out: dict = {}
    if "resources" in value:
        import capo_ram.types.resource_list

        out["resources"] = capo_ram.types.resource_list.serialize_json(
            value["resources"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPendingInvitationResourcesResponse:
    out: ListPendingInvitationResourcesResponse = {}  # type: ignore[typeddict-item]
    if "resources" in data:
        import capo_ram.types.resource_list

        out["resources"] = capo_ram.types.resource_list.deserialize_json(
            data["resources"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
