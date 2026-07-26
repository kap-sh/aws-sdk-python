"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListProposalsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.pagination_token
    import capo_managedblockchain.types.proposal_summary_list


class ListProposalsOutput(TypedDict, closed=True):
    proposals: NotRequired[
        "capo_managedblockchain.types.proposal_summary_list.ProposalSummaryList"
    ]
    """<p>The summary of each proposal made on the network.</p>"""
    next_token: NotRequired[
        "capo_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProposalsOutput) -> dict:
    out: dict = {}
    if "proposals" in value:
        import capo_managedblockchain.types.proposal_summary_list

        out["Proposals"] = (
            capo_managedblockchain.types.proposal_summary_list.serialize_json(
                value["proposals"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProposalsOutput:
    out: ListProposalsOutput = {}  # type: ignore[typeddict-item]
    if "Proposals" in data:
        import capo_managedblockchain.types.proposal_summary_list

        out["proposals"] = (
            capo_managedblockchain.types.proposal_summary_list.deserialize_json(
                data["Proposals"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
