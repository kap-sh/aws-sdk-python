"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateProposalOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class CreateProposalOutput(TypedDict):
    proposal_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the proposal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProposalOutput) -> dict:
    out: dict = {}
    if "proposal_id" in value:
        out["ProposalId"] = value["proposal_id"]
    return out


def deserialize_json(data: dict) -> CreateProposalOutput:
    out: CreateProposalOutput = {}  # type: ignore[typeddict-item]
    if "ProposalId" in data:
        out["proposal_id"] = data["ProposalId"]
    return out
