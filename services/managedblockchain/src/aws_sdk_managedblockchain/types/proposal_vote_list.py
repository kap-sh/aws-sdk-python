"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ProposalVoteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.vote_summary

ProposalVoteList: TypeAlias = list[
    "aws_sdk_managedblockchain.types.vote_summary.VoteSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProposalVoteList) -> list:
    import aws_sdk_managedblockchain.types.vote_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_managedblockchain.types.vote_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProposalVoteList:
    import aws_sdk_managedblockchain.types.vote_summary

    out: ProposalVoteList = []
    for item in data:
        out.append(aws_sdk_managedblockchain.types.vote_summary.deserialize_json(item))
    return out
