"""Generated from Smithy shape ``com.amazonaws.ram#AcceptResourceShareInvitationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.resource_share_invitation
    import aws_sdk_ram.types.string


class AcceptResourceShareInvitationResponse(TypedDict):
    resource_share_invitation: NotRequired[
        "aws_sdk_ram.types.resource_share_invitation.ResourceShareInvitation"
    ]
    """<p>An object that contains information about the specified invitation.</p>"""
    client_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptResourceShareInvitationResponse) -> dict:
    out: dict = {}
    if "resource_share_invitation" in value:
        import aws_sdk_ram.types.resource_share_invitation

        out["resourceShareInvitation"] = (
            aws_sdk_ram.types.resource_share_invitation.serialize_json(
                value["resource_share_invitation"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AcceptResourceShareInvitationResponse:
    out: AcceptResourceShareInvitationResponse = {}  # type: ignore[typeddict-item]
    if "resourceShareInvitation" in data:
        import aws_sdk_ram.types.resource_share_invitation

        out["resource_share_invitation"] = (
            aws_sdk_ram.types.resource_share_invitation.deserialize_json(
                data["resourceShareInvitation"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
