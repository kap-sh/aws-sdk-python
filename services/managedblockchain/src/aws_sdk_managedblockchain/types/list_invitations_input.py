"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListInvitationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.pagination_token
    import aws_sdk_managedblockchain.types.proposal_list_max_results


class ListInvitationsInput(TypedDict):
    max_results: NotRequired[
        "aws_sdk_managedblockchain.types.proposal_list_max_results.ProposalListMaxResults"
    ]
    """<p>The maximum number of invitations to return.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvitationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInvitationsInput:
    out: ListInvitationsInput = {}  # type: ignore[typeddict-item]
    return out
