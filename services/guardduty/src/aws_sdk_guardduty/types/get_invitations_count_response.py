"""Generated from Smithy shape ``com.amazonaws.guardduty#GetInvitationsCountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer


class GetInvitationsCountResponse(TypedDict):
    invitations_count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The number of received invitations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvitationsCountResponse) -> dict:
    out: dict = {}
    if "invitations_count" in value:
        out["invitationsCount"] = value["invitations_count"]
    return out


def deserialize_json(data: dict) -> GetInvitationsCountResponse:
    out: GetInvitationsCountResponse = {}  # type: ignore[typeddict-item]
    if "invitationsCount" in data:
        out["invitations_count"] = data["invitationsCount"]
    return out
