"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListProposalVotesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.pagination_token
    import capo_managedblockchain.types.proposal_list_max_results
    import capo_managedblockchain.types.resource_id_string


class ListProposalVotesInput(TypedDict, closed=True):
    network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p> The unique identifier of the network. </p>"""
    proposal_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p> The unique identifier of the proposal. </p>"""
    max_results: NotRequired[
        "capo_managedblockchain.types.proposal_list_max_results.ProposalListMaxResults"
    ]
    """<p> The maximum number of votes to return. </p>"""
    next_token: NotRequired[
        "capo_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p> The pagination token that indicates the next set of results to retrieve. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProposalVotesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProposalVotesInput:
    out: ListProposalVotesInput = {}  # type: ignore[typeddict-item]
    return out
