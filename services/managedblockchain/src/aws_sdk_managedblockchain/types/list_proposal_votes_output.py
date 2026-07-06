"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListProposalVotesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.pagination_token
    import aws_sdk_managedblockchain.types.proposal_vote_list


class ListProposalVotesOutput(TypedDict, closed=True):
    proposal_votes: NotRequired[
        "aws_sdk_managedblockchain.types.proposal_vote_list.ProposalVoteList"
    ]
    """<p> The list of votes. </p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p> The pagination token that indicates the next set of results to retrieve. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProposalVotesOutput) -> dict:
    out: dict = {}
    if "proposal_votes" in value:
        import aws_sdk_managedblockchain.types.proposal_vote_list

        out["ProposalVotes"] = (
            aws_sdk_managedblockchain.types.proposal_vote_list.serialize_json(
                value["proposal_votes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProposalVotesOutput:
    out: ListProposalVotesOutput = {}  # type: ignore[typeddict-item]
    if "ProposalVotes" in data:
        import aws_sdk_managedblockchain.types.proposal_vote_list

        out["proposal_votes"] = (
            aws_sdk_managedblockchain.types.proposal_vote_list.deserialize_json(
                data["ProposalVotes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
