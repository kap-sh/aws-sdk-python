"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListProposalsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.pagination_token
    import aws_sdk_managedblockchain.types.proposal_summary_list


class ListProposalsOutput(TypedDict):
    proposals: NotRequired[
        "aws_sdk_managedblockchain.types.proposal_summary_list.ProposalSummaryList"
    ]
    """<p>The summary of each proposal made on the network.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProposalsOutput) -> dict:
    out: dict = {}
    if "proposals" in value:
        import aws_sdk_managedblockchain.types.proposal_summary_list

        out["Proposals"] = (
            aws_sdk_managedblockchain.types.proposal_summary_list.serialize_json(
                value["proposals"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProposalsOutput:
    out: ListProposalsOutput = {}  # type: ignore[typeddict-item]
    if "Proposals" in data:
        import aws_sdk_managedblockchain.types.proposal_summary_list

        out["proposals"] = (
            aws_sdk_managedblockchain.types.proposal_summary_list.deserialize_json(
                data["Proposals"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
