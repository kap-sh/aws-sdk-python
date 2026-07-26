"""Generated from Smithy shape ``com.amazonaws.ram#GetResourceShareInvitationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.resource_share_invitation_list
    import capo_ram.types.string


class GetResourceShareInvitationsResponse(TypedDict, closed=True):
    resource_share_invitations: NotRequired[
        "capo_ram.types.resource_share_invitation_list.ResourceShareInvitationList"
    ]
    """<p>An array of objects that contain the details about the invitations.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceShareInvitationsResponse) -> dict:
    out: dict = {}
    if "resource_share_invitations" in value:
        import capo_ram.types.resource_share_invitation_list

        out["resourceShareInvitations"] = (
            capo_ram.types.resource_share_invitation_list.serialize_json(
                value["resource_share_invitations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetResourceShareInvitationsResponse:
    out: GetResourceShareInvitationsResponse = {}  # type: ignore[typeddict-item]
    if "resourceShareInvitations" in data:
        import capo_ram.types.resource_share_invitation_list

        out["resource_share_invitations"] = (
            capo_ram.types.resource_share_invitation_list.deserialize_json(
                data["resourceShareInvitations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
