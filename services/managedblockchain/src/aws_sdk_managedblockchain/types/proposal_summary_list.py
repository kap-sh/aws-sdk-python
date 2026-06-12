"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ProposalSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.proposal_summary

ProposalSummaryList: TypeAlias = list[
    "aws_sdk_managedblockchain.types.proposal_summary.ProposalSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProposalSummaryList) -> list:
    import aws_sdk_managedblockchain.types.proposal_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_managedblockchain.types.proposal_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProposalSummaryList:
    import aws_sdk_managedblockchain.types.proposal_summary

    out: ProposalSummaryList = []
    for item in data:
        out.append(
            aws_sdk_managedblockchain.types.proposal_summary.deserialize_json(item)
        )
    return out
