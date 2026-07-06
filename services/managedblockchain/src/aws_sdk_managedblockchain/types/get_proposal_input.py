"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetProposalInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class GetProposalInput(TypedDict, closed=True):
    network_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network for which the proposal is made.</p>"""
    proposal_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the proposal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProposalInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProposalInput:
    out: GetProposalInput = {}  # type: ignore[typeddict-item]
    return out
