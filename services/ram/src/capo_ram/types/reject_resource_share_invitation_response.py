"""Generated from Smithy shape ``com.amazonaws.ram#RejectResourceShareInvitationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.resource_share_invitation
    import capo_ram.types.string


class RejectResourceShareInvitationResponse(TypedDict, closed=True):
    resource_share_invitation: NotRequired[
        "capo_ram.types.resource_share_invitation.ResourceShareInvitation"
    ]
    """<p>An object that contains the details about the rejected invitation.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectResourceShareInvitationResponse) -> dict:
    out: dict = {}
    if "resource_share_invitation" in value:
        import capo_ram.types.resource_share_invitation

        out["resourceShareInvitation"] = (
            capo_ram.types.resource_share_invitation.serialize_json(
                value["resource_share_invitation"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RejectResourceShareInvitationResponse:
    out: RejectResourceShareInvitationResponse = {}  # type: ignore[typeddict-item]
    if "resourceShareInvitation" in data:
        import capo_ram.types.resource_share_invitation

        out["resource_share_invitation"] = (
            capo_ram.types.resource_share_invitation.deserialize_json(
                data["resourceShareInvitation"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
