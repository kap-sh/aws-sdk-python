"""Generated from Smithy shape ``com.amazonaws.macie2#GetInvitationsCountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long


class GetInvitationsCountResponse(TypedDict, closed=True):
    invitations_count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of invitations that were received by the account, not including the currently accepted invitation.</p>"""


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
