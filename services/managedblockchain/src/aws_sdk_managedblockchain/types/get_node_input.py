"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetNodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class GetNodeInput(TypedDict, closed=True):
    network_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network that the node is on.</p>"""
    member_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the member that owns the node.</p> <p>Applies only to Hyperledger Fabric and is required for Hyperledger Fabric.</p>"""
    node_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNodeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNodeInput:
    out: GetNodeInput = {}  # type: ignore[typeddict-item]
    return out
