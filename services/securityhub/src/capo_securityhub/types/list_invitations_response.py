"""Generated from Smithy shape ``com.amazonaws.securityhub#ListInvitationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.invitation_list
    import capo_securityhub.types.non_empty_string


class ListInvitationsResponse(TypedDict, closed=True):
    invitations: NotRequired["capo_securityhub.types.invitation_list.InvitationList"]
    """<p>The details of the invitations returned by the operation.</p>"""
    next_token: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The pagination token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvitationsResponse) -> dict:
    out: dict = {}
    if "invitations" in value:
        import capo_securityhub.types.invitation_list

        out["Invitations"] = capo_securityhub.types.invitation_list.serialize_json(
            value["invitations"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvitationsResponse:
    out: ListInvitationsResponse = {}  # type: ignore[typeddict-item]
    if "Invitations" in data:
        import capo_securityhub.types.invitation_list

        out["invitations"] = capo_securityhub.types.invitation_list.deserialize_json(
            data["Invitations"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
