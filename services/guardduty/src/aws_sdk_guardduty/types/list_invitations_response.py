"""Generated from Smithy shape ``com.amazonaws.guardduty#ListInvitationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.invitations
    import aws_sdk_guardduty.types.string


class ListInvitationsResponse(TypedDict):
    invitations: NotRequired["aws_sdk_guardduty.types.invitations.Invitations"]
    """<p>A list of invitation descriptions.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvitationsResponse) -> dict:
    out: dict = {}
    if "invitations" in value:
        import aws_sdk_guardduty.types.invitations

        out["invitations"] = aws_sdk_guardduty.types.invitations.serialize_json(
            value["invitations"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvitationsResponse:
    out: ListInvitationsResponse = {}  # type: ignore[typeddict-item]
    if "invitations" in data:
        import aws_sdk_guardduty.types.invitations

        out["invitations"] = aws_sdk_guardduty.types.invitations.deserialize_json(
            data["invitations"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
