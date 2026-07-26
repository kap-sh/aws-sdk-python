"""Generated from Smithy shape ``com.amazonaws.macie2#AcceptInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string


class AcceptInvitationRequest(TypedDict, closed=True):
    administrator_account_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the account that sent the invitation.</p>"""
    invitation_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the invitation to accept.</p>"""
    master_account: NotRequired["capo_macie2.types.__string.__string"]
    """<p>(Deprecated) The Amazon Web Services account ID for the account that sent the invitation. This property has been replaced by the administratorAccountId property and is retained only for backward compatibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptInvitationRequest) -> dict:
    out: dict = {}
    if "administrator_account_id" in value:
        out["administratorAccountId"] = value["administrator_account_id"]
    if "invitation_id" in value:
        out["invitationId"] = value["invitation_id"]
    if "master_account" in value:
        out["masterAccount"] = value["master_account"]
    return out


def deserialize_json(data: dict) -> AcceptInvitationRequest:
    out: AcceptInvitationRequest = {}  # type: ignore[typeddict-item]
    if "administratorAccountId" in data:
        out["administrator_account_id"] = data["administratorAccountId"]
    if "invitationId" in data:
        out["invitation_id"] = data["invitationId"]
    if "masterAccount" in data:
        out["master_account"] = data["masterAccount"]
    return out
