"""Generated from Smithy shape ``com.amazonaws.macie2#ListInvitationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_invitation
    import aws_sdk_macie2.types.__string


class ListInvitationsResponse(TypedDict):
    invitations: NotRequired[
        "aws_sdk_macie2.types.__list_of_invitation.__listOfInvitation"
    ]
    """<p>An array of objects, one for each invitation that was received by the account.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvitationsResponse) -> dict:
    out: dict = {}
    if "invitations" in value:
        import aws_sdk_macie2.types.__list_of_invitation

        out["invitations"] = aws_sdk_macie2.types.__list_of_invitation.serialize_json(
            value["invitations"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvitationsResponse:
    out: ListInvitationsResponse = {}  # type: ignore[typeddict-item]
    if "invitations" in data:
        import aws_sdk_macie2.types.__list_of_invitation

        out["invitations"] = aws_sdk_macie2.types.__list_of_invitation.deserialize_json(
            data["invitations"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
