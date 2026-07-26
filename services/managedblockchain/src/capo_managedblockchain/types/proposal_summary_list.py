"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ProposalSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain.types.proposal_summary

ProposalSummaryList: TypeAlias = list[
    "capo_managedblockchain.types.proposal_summary.ProposalSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProposalSummaryList) -> list:
    import capo_managedblockchain.types.proposal_summary

    out: list = []
    for item in value:
        out.append(capo_managedblockchain.types.proposal_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProposalSummaryList:
    import capo_managedblockchain.types.proposal_summary

    out: ProposalSummaryList = []
    for item in data:
        out.append(capo_managedblockchain.types.proposal_summary.deserialize_json(item))
    return out
