"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListProposalVotesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.pagination_token
    import capo_managedblockchain.types.proposal_vote_list


class ListProposalVotesOutput(TypedDict, closed=True):
    proposal_votes: NotRequired[
        "capo_managedblockchain.types.proposal_vote_list.ProposalVoteList"
    ]
    """<p> The list of votes. </p>"""
    next_token: NotRequired[
        "capo_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p> The pagination token that indicates the next set of results to retrieve. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProposalVotesOutput) -> dict:
    out: dict = {}
    if "proposal_votes" in value:
        import capo_managedblockchain.types.proposal_vote_list

        out["ProposalVotes"] = (
            capo_managedblockchain.types.proposal_vote_list.serialize_json(
                value["proposal_votes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProposalVotesOutput:
    out: ListProposalVotesOutput = {}  # type: ignore[typeddict-item]
    if "ProposalVotes" in data:
        import capo_managedblockchain.types.proposal_vote_list

        out["proposal_votes"] = (
            capo_managedblockchain.types.proposal_vote_list.deserialize_json(
                data["ProposalVotes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
