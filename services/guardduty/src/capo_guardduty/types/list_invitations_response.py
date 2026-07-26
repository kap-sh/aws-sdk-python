"""Generated from Smithy shape ``com.amazonaws.guardduty#ListInvitationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.invitations
    import capo_guardduty.types.string


class ListInvitationsResponse(TypedDict, closed=True):
    invitations: NotRequired["capo_guardduty.types.invitations.Invitations"]
    """<p>A list of invitation descriptions.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvitationsResponse) -> dict:
    out: dict = {}
    if "invitations" in value:
        import capo_guardduty.types.invitations

        out["invitations"] = capo_guardduty.types.invitations.serialize_json(
            value["invitations"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvitationsResponse:
    out: ListInvitationsResponse = {}  # type: ignore[typeddict-item]
    if "invitations" in data:
        import capo_guardduty.types.invitations

        out["invitations"] = capo_guardduty.types.invitations.deserialize_json(
            data["invitations"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
