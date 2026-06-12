"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListInvitationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.invitation_list
    import aws_sdk_managedblockchain.types.pagination_token


class ListInvitationsOutput(TypedDict):
    invitations: NotRequired[
        "aws_sdk_managedblockchain.types.invitation_list.InvitationList"
    ]
    """<p>The invitations for the network.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvitationsOutput) -> dict:
    out: dict = {}
    if "invitations" in value:
        import aws_sdk_managedblockchain.types.invitation_list

        out["Invitations"] = (
            aws_sdk_managedblockchain.types.invitation_list.serialize_json(
                value["invitations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvitationsOutput:
    out: ListInvitationsOutput = {}  # type: ignore[typeddict-item]
    if "Invitations" in data:
        import aws_sdk_managedblockchain.types.invitation_list

        out["invitations"] = (
            aws_sdk_managedblockchain.types.invitation_list.deserialize_json(
                data["Invitations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
