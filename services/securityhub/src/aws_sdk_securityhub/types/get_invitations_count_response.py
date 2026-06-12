"""Generated from Smithy shape ``com.amazonaws.securityhub#GetInvitationsCountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer


class GetInvitationsCountResponse(TypedDict):
    invitations_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of all membership invitations sent to this Security Hub CSPM member account, not including the currently accepted invitation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvitationsCountResponse) -> dict:
    out: dict = {}
    if "invitations_count" in value:
        out["InvitationsCount"] = value["invitations_count"]
    return out


def deserialize_json(data: dict) -> GetInvitationsCountResponse:
    out: GetInvitationsCountResponse = {}  # type: ignore[typeddict-item]
    if "InvitationsCount" in data:
        out["invitations_count"] = data["InvitationsCount"]
    return out
