"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetProposalOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.proposal


class GetProposalOutput(TypedDict, closed=True):
    proposal: NotRequired["capo_managedblockchain.types.proposal.Proposal"]
    """<p>Information about a proposal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProposalOutput) -> dict:
    out: dict = {}
    if "proposal" in value:
        import capo_managedblockchain.types.proposal

        out["Proposal"] = capo_managedblockchain.types.proposal.serialize_json(
            value["proposal"]
        )
    return out


def deserialize_json(data: dict) -> GetProposalOutput:
    out: GetProposalOutput = {}  # type: ignore[typeddict-item]
    if "Proposal" in data:
        import capo_managedblockchain.types.proposal

        out["proposal"] = capo_managedblockchain.types.proposal.deserialize_json(
            data["Proposal"]
        )
    return out
