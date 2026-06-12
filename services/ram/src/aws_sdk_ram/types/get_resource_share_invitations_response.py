"""Generated from Smithy shape ``com.amazonaws.ram#GetResourceShareInvitationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.resource_share_invitation_list
    import aws_sdk_ram.types.string


class GetResourceShareInvitationsResponse(TypedDict):
    resource_share_invitations: NotRequired[
        "aws_sdk_ram.types.resource_share_invitation_list.ResourceShareInvitationList"
    ]
    """<p>An array of objects that contain the details about the invitations.</p>"""
    next_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceShareInvitationsResponse) -> dict:
    out: dict = {}
    if "resource_share_invitations" in value:
        import aws_sdk_ram.types.resource_share_invitation_list

        out["resourceShareInvitations"] = (
            aws_sdk_ram.types.resource_share_invitation_list.serialize_json(
                value["resource_share_invitations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetResourceShareInvitationsResponse:
    out: GetResourceShareInvitationsResponse = {}  # type: ignore[typeddict-item]
    if "resourceShareInvitations" in data:
        import aws_sdk_ram.types.resource_share_invitation_list

        out["resource_share_invitations"] = (
            aws_sdk_ram.types.resource_share_invitation_list.deserialize_json(
                data["resourceShareInvitations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
