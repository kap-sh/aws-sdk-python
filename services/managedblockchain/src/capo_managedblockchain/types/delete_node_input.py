"""Generated from Smithy shape ``com.amazonaws.managedblockchain#DeleteNodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.resource_id_string


class DeleteNodeInput(TypedDict, closed=True):
    network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network that the node is on.</p> <p>Ethereum public networks have the following <code>NetworkId</code>s:</p> <ul> <li> <p> <code>n-ethereum-mainnet</code> </p> </li> </ul>"""
    member_id: NotRequired[
        "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the member that owns this node.</p> <p>Applies only to Hyperledger Fabric and is required for Hyperledger Fabric.</p>"""
    node_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNodeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNodeInput:
    out: DeleteNodeInput = {}  # type: ignore[typeddict-item]
    return out
